**HAMILTONIAN MONTE CARLO (HMC)**

---

**Contents**:

- [Motivation](#motivation)
- [Notation](#notation)
- [Key concepts](#key-concepts)
  - [Momentum](#momentum)
  - [Hamiltonian (i.e. Hamiltonian function)](#hamiltonian-ie-hamiltonian-function)
    - [PRELIMINARY TOPIC: Hamilton's equations of motion](#preliminary-topic-hamiltons-equations-of-motion)
    - [MAIN TOPIC: Hamiltonian function](#main-topic-hamiltonian-function)
- [Further conceptual clarity on HMC](#further-conceptual-clarity-on-hmc)
- [Mathematical formulation](#mathematical-formulation)
  - [PRELIMINARY POINT: The goal of using a sampling method](#preliminary-point-the-goal-of-using-a-sampling-method)
  - [MAIN TOPIC: Mathematical formulation of HMC](#main-topic-mathematical-formulation-of-hmc)
- [Algorithm and practical computation](#algorithm-and-practical-computation)
  - [Essential steps](#essential-steps)
  - [Metropolis acceptance criterion for HMC](#metropolis-acceptance-criterion-for-hmc)
- [Additional points about HMC](#additional-points-about-hmc)

---

**NOTE**: _HMC is a class of methods, rather than a single method._

---

**Abbreviations**:

- HMC: Hamiltonian Monte Carlo
- MCMC: Markov chain Monte Carlo

---

# Motivation
**_Why is HMC important?_**

HMC is a class of MCMC methods that uses gradients (of the negative log-probability of the posterior distribution) to generate new proposed states (i.e. new samples proposed to be from the target distribution). The gradients of the negative log-probability of the posterior evaluated at a given state (i.e. a given sample) gives information about the posterior density function's geometry.

_Why is the negative log-probability of the posterior used, rather than the posterior itself?_ The mathematical basis for it shall become clear in the subsection ["Mathematical formulation"](#mathematical-formulation). However, note that the negative log-probability preserves the distribution of the posterior's probability mass as well as the posterior's modes, except that the modes are represented by minima instead of maxima. Hence, samples from a high-probability-mass region of the negative log-probability of the posterior follow the same distribution as samples from a high-probability-mass region of the posterior itself.

HMC tries to avoid the random walk behavior typical of Metropolis-Hastings by using the gradient to propose new positions (i.e. new samples) that is both far from the current position (i.e. current sample) and with high acceptance probability. This allows HMC to better scale to higher dimensions and, in principle, to more complex geometries (compared to alternative methods). Intuitively, we can think of HMC as a Metropolis-Hasting algorithm with a better sample proposal distribution.

---

There are three benefits of consistently proposing new positions that are both far from the current position and with high acceptance rate: (1) You are likely to gain a much more representative and thus accurate sample of the distribution you want to estimate, but using fewer sampled values; in other words, it tends to make sampling more efficient. (2) You can explore multimodal distributions more effectively (see: ["MCMC vs. multimodal distributions"](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc/README.md#mcmc-vs-multimodal-distributions)). (3) You speed up mixing, i.e. generating a Markov chain with less correlated samples, thus partially overcoming the main disadvantage of MCMC methods, namely that the samples are not uncorrelated.  This helps converge to the target distribution faster, especially for higher dimensional target distributions (reference: [_Training BNNs with HMC_ from **janosh.dev**](https://janosh.dev/posts/hmc-bnn)).

---

**NOTE 1**: Remember that a "sample" here is a tuple of one or more values proposed parameter values of the target distribution. What we are trying to do, here and in all sampling methods, is discover (with some level of uncertainty) how well the various potential parameter values would describe the target distribution. Note also that a "position" or a "state" is simply a sample, i.e. simply a proposed tuple of parameter values.

**NOTE 2**: Sampling from the negative log-probability of the posterior is the same in effect as sampling from the posterior itself (i.e. both lead to samples following the same distribution). Hence, when I refer to sampling from the posterior in the context of HMC, note that I am referring more precisely to sampling from the negative log-probability of the posterior. The distinction is only needed to describe the specific process of HMC and does not reflect on the actual samples obtained. However, apart from describing the specific process of HMC, I find that speaking in terms of sampling from the posterior makes it easier to relate the conceptual basis of HMC (i.e. Hamiltonian mechanics) to posterior sampling, which is why, when possible, I prefer to speak of sampling from the posterior rather than sampling from the negative log-probability of the posterior.

---

As we shall see, HMC is inspired from Hamiltonian mechanics and is hence often explained with an analogy to classical mechanics. In the context of HMC context, the "position" of the sample can be thought of as the location of a particle, and the "momentum" provides the force needed to move the particle through the parameter space.

# Notation
- Let $p$ denote the target distribution
- Let $\theta$ denote a particular position (i.e. state/sample)
- Let $m$ denote the "momentum" parameter (to be defined soon)
- Let $D$ denote the observed data

# Key concepts
## Momentum
$m$ , i.e. the "momentum", denotes a parameter used to alter how the Markov chian moves along the gradients (i.e. along the shape of the function corresponding to an approximation of the posterior) to the next state/sample. Why would alter such movement? Because we are not interested in following the gradient toward the mode (i.e. the peak, i.e. the hill, i.e. the local optimum), but rather, we are interested in exploring the high-probability-mass region of the posterior. _How high is high enough? Depends on our purposes_.

The analogy commonly used to describe HMC is based on classical mechanics. Let us use the analogy of a planet whose centre is the mode, with its gravitational pull forming a field of force vectors leading into the centre. Our goal is not to follow the force vectors toward the centre, but rather, our goal is to explore the space around the planet where the gravity is high enough (with respect to our purposes). In cases with multiple models (i.e. multimodal posteriors), we can think of a space with multiple planets fixed in place while each exerts its own gravitational pull.

"Momentum" in the context of HMC is analogous to the physical momentum given to a body in space so that it follows a certain orbital trajectory rather than a trajectory that goes directly toward the planet's centre. More precisely, it is an auxiliary variable that ensures that the Markov chain sampling (done based on following the gradient) samples from a sufficiently high-probability-mass region of the posterior rather than moving toward the posterior distribution's mode.

**NOTE**: _Momentum is a vector quantity and can be multi-dimensional. A one-dimensional momentum (a single value) is the momentum of a body along a line, a two-dimensional momentum (a vector of two values) is the momentum of a body across a plane, a three-dimensional momentum (a vector of three values) is the momentum of a body across a space, etc._

---

> **Reference (especially for the analogy**): [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ by London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)

## Hamiltonian (i.e. Hamiltonian function)
### PRELIMINARY TOPIC: Hamilton's equations of motion
This is a function based on the Hamilton's equations of motion (see: ["14.3: Hamilton's Equations of Motion" from _Hamiltonian Mechanics_ from _Classical Mechanics (Tatum)_ from **Classical Mechanics**, **LibreTexts Physics**](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Classical_Mechanics_(Tatum)/14%3A_Hamiltonian_Mechanics/14.03%3A_Hamilton%27s_Equations_of_Motion)), which describe the state of a physical system with one body of a fixed mass moving in a space of $k$ dimensions ($k \geq 1$). In essence, Hamilton's equations of motion describe any system's temporal evolution that can be defined with a Hamiltonian function, signifying the total energy of the system.

---

**NOTE 1**: Hamilton's equations of motion only consider the motion of a single body, and do not explicitly take into account interactions with another body or with a surface. However, interactions with other bodies can be described using changes in momentum. Hence, we can take into account interactions (e.g. collisions, gravitational force, a force field, etc.) as functions of the momentum. In the context of HMC, the "body" would be the imaginary point of the sampler, with two kinds of forces being exerted on it: an imaginary momentum and the contours of the posterior distribution.

**NOTE 2**: Hamilton's equations of motion can apply for any number of dimensions, even though in physics, we would only deal with three dimensions. Hence, in a multidimensional function, e.g. a posterior distribution of the parameters of a neural network, Hamilton's equations would still apply despite the high dimensionality of the space.

**NOTE 3**: Even though Hamilton's equations were meant to deal with physical spaces, we can accurately extend their application to analogous simulated or abstract spaces, such as a high-dimensional sample space for the values of a model's parameters. Hence, they provide a valid basis for exploring the posterior distribution and sampling from it more diversely and efficiently.

### MAIN TOPIC: Hamiltonian function
Consider a system $S$ of $k$ dimensions with coordinates $\theta_1, \theta_2 ... \theta_k$ and dimension-specific momenta $m_1, m_2 ... m_k$ (i.e. each coordinate $\theta_i$ is associated with the momentum $m_i$). Let $\theta$ be the position defined by the $k$ coordinates, and let $m$ be the overall (i.e. $k$-dimensional) momentum of the body at $\theta$. Hamilton's equations are derived from a function of the position $\theta$ and the momentum $m$. This function is known as the Hamiltonian. The Hamiltonian, represented by $H(\theta, m)$, amounts to the total energy of the system $S$. Note that we assume that the system is self-contained, and hence, that the system's total energy is constant. Hence, $H(\theta, m)$ is constant, even as the position and momentum change. More precisely, we have that:

$H(\theta, m) = K(\theta) + V(\theta) =$ _constant_

Here:

- $K(m)$: System's total kinetic energy (independent of position)
- $V(\theta)$: System's total potential energy (independent of momentum)

---

Using the Hamiltonian, we write Hamilton's equations of motion:

**Equation 1**:

$\frac{d \theta}{dt} = \frac{\delta H}{\delta m} = \frac{\delta K}{\delta m} + \frac{\delta V}{\delta m} = \frac{\delta K}{\delta m}$

**NOTE**: $\frac{\delta V}{\delta m} = 0$

Hence, we have equation 1 as $\frac{d \theta}{dt} = \frac{\delta K}{\delta m}$

**Equation 2**:

$\frac{dm}{dt} = - \frac{\delta H}{\delta \theta} = - \frac{\delta K}{\delta \theta} - \frac{\delta V}{\delta \theta} = - \frac{\delta V}{\delta \theta}$

**NOTE**: $\frac{\delta K}{\delta \theta} = 0$

Hence, we have equation 2 as $\frac{dm}{dt} = - \frac{\delta V}{\delta \theta}$

---

Note that in the above equations:

- $\frac{d \theta}{dt}$ = Change in position with respect to unit change in time
- $\frac{dm}{dt}$ = Change in momentum with respect to unit change in time

Hence, solving the above equations, we can simulate the system $S$; for example, given the initial position $\theta$ and initial momentum $m$, we can figure out the change in the position and momentum across time. Hence, using Hamilton's equations of motion in such a way, and using our knowledge of the forces acting on the body (describable as functions of the momentum), we can figure out how the body in the system would move over time. In the case of using Hamilton's equations of motion for sampling from a posterior (the phrase "sampling from a posterior" is explained in the next section), the forces are an imaginary momentum and the contours of the posterior distribution, both acting upon an imaginary point representing the sampler.

**NOTE**: _The "forces" described in the context of HMC are meant to guide the efficient exploration of the posterior distribution. The contours of the posterior are fixed, so the only thing we can adjust to improve the sampler's performance is the momentum._

---

> **References**:
>
> - [_Hamiltonian Monte Carlo For Dummies (Statisticians / Pharmacometricians / All)_ by Alan Maloney, **YouTube**](https://www.youtube.com/watch?v=ZGtezhDaSpM)
> - [_Hamilton's Equations of Motion_ from **StudySmarter.co.uk**](https://www.studysmarter.co.uk/explanations/physics/classical-mechanics/hamiltons-equations-of-motion)

# Further conceptual clarity on HMC
_A Conceptual Introduction to Hamiltonian Monte Carlo_ by Michael Betancourt:

- **Paper**: https://arxiv.org/pdf/1701.02434
- **Notes**: [`a-conceptual-introduction-to-hamiltonian-monte-carlo.md`](https://github.com/pranigopu/mastersProject/blob/main/reading/a-conceptual-introduction-to-hamiltonian-monte-carlo.md)

_The notes contain key excerpts, a helpful organisation of ideas and clarifying comments._

# Mathematical formulation
## PRELIMINARY POINT: The goal of using a sampling method
The whole point of a sampling method is to estimate an unknown distribution. Hence, in practice, when we sample from the posterior, it is because we do not know the posterior. However, due to certain theoretical guarantees in the general MCMC approach (mainly the guarantee that the steady-state transition probabilities of the sampler's Markov chain simulate the posterior distribution; see: [_Markov chain Monte Carlo (MCMC)_](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc)), we have that after a certain number of samples, we begin to draw samples as if from the posterior. Hence, when we say "sample from the posterior", we mean that in the way described by the general MCMC approach. How HMC in implements the general MCMC approach is what we shall see now.

## MAIN TOPIC: Mathematical formulation of HMC
Let us first define the following:

- $P$, the measure of probability density or mass (depending on context)
- $\theta$, the position, i.e. the sample taken from the posterior
- $\Theta$, the sample space of positions
- $p$, the target distribution, i.e. the posterior distribution
- $m$, the momentum applied to the imaginary sampler point at position $\theta$

**NOTE**: $\theta$ _denotes a specific parametrisation of the generalised model which we are trying to fit to the data. Hence, since models are usually parametrised by more than one specific parameter,_ $\theta$ _is usually a vector of specific parameters._ $\Theta$ _denotes the hypothesis space, i.e. the set of all possible parametrisations considered by us of the generalised model. Hence, note that_ $\theta$ _represents a specific model, whereas_ $\Theta$ _represents the sample space of specific models, each being a specific parametrisation of the generalised model. Also note that if_ $\theta$ _is k-dimensional (i.e. has k elements, denoting k specific parameters), then_ $\Theta$ _is a k-dimensional sample space, and consequently, we are dealing with "positions" and "momentum" in a k-dimensional space._

---

**What do we need to find?**

- $p = P(\theta|D)$, the target distribution, i.e. the posterior distribution

**What do we have available?**

- $D$, dataset of observations (from the data-generation process we are trying to model)
- $P(D|\theta)$, the likelihood of dataset $D$ given the model parametrised by $\theta$
- $P(\theta)$, the prior distribution of $\theta$ defined before the inference
- $P(m)$, the distribution of momentum values chosen by us

**What do we know?**

- $\displaystyle P(\theta|D) = \frac{P(D|\theta) P(\theta)}{\int_{\theta' \in \Theta} P(\theta', D) d\theta'} \propto P(D|\theta) P(\theta)$
- $P(\theta, m) = P(\theta|D) P(m)$

**What we do not know in practice**:

- $\displaystyle \int_{\theta' \in \Theta} P(\theta', D) d\theta'$, the denominator or "evidence" in Bayesian inference

**NOTE**: _Of course, if we knew the denominator, the posterior_ $p = P(\theta|D)$ _would already by known._

---

Why bother with the joint distribution? Because of the following:

$P(\theta, m) = P(\theta|D) P(m)$

$\implies \log P(\theta, m) = \log (P(\theta|D) P(m)) = \log P(\theta|D) + \log P(m)$

$\implies - \log P(\theta, m) = - \log P(\theta|D) - \log P(m)$

The above equation is in the form of a Hamiltonian, where:

- $H(\theta, m) = - \log P(\theta, m)$
- $K(m) = - \log P(m)$ ("kinetic energy")
- $V(\theta) = - \log P(\theta|D)$ ("potential energy")

---

**NOTE**:

- Probabilities are always between 0 and 1
- Hence, the logarithms of probabilities are always less than or equal to 0
- Hence, negative logarithms of probabilities are always $\geq$ to 0
- Hence, the physical motion-based analogy is valid
- Hence means that Hamilton's equations of motion will work as intended

---

**REMINDER**:

Hamiltonian's equations are as follows:

Equation 1:

$\frac{d \theta}{dt} = \frac{\delta H}{\delta m} = \frac{\delta K}{\delta m} + \frac{\delta V}{\delta m} = \frac{\delta K}{\delta m}$ (because $\frac{\delta V}{\delta m} = 0$)

i.e.

$\frac{d \theta}{dt} = \frac{\delta K}{\delta m}$

Equation 2:

$\frac{dm}{dt} = - \frac{\delta H}{\delta \theta} = - \frac{\delta K}{\delta \theta} - \frac{\delta V}{\delta \theta} = - \frac{\delta V}{\delta \theta}$ (because $\frac{\delta K}{\delta \theta} = 0$)

i.e.

$\frac{dm}{dt} = - \frac{\delta V}{\delta \theta}$

---

We know that $\displaystyle P(\theta|D) = \frac{P(D|\theta) P(\theta)}{\int_{\theta' \in \Theta} P(\theta', D) d\theta'}$

$\implies \log P(\theta|D) = \log \frac{P(D|\theta) P(\theta)}{\int_{\theta' \in \Theta} P(\theta', D) d\theta'} = \log(P(D|\theta) P(\theta)) - \log(\int_{\theta' \in \Theta} P(\theta', D) d\theta')$

---

For convenience, put $\displaystyle z = \int_{\theta' \in \Theta} P(\theta', D) d\theta'$. Hence:

$V(\theta) = - \log P(\theta|D) = - \log(P(D|\theta) P(\theta)) + \log z$

---

But note that $z$ marginalises out the position $\theta$. Hence, $z$ is independent of position $\theta$.

$\implies \frac{\delta V}{\delta \theta} = \frac{\delta (- \log(P(D|\theta) P(\theta)))}{\delta \theta} + 0 = - \frac{\delta \log(P(D|\theta) P(\theta))}{\delta \theta}$

**NOTE**: $\frac{dm}{dt} = - \frac{\delta V}{\delta \theta} \implies \frac{\delta V}{\delta \theta}$ _determines momentum change across time steps (i.e. across sampling steps)._

---

**What do we need to find?**

- The target distribution, i.e. the posterior distribution $p = P(\theta|D)$

**What do we have available?**

- $K(m) = - \log P(m)$, since we already have $P(m)$
- $\frac{\delta \theta}{\delta t} = \frac{\delta K}{\delta m}$, since we already have $K(m)$
- $H = - \log P(\theta, m)$, since we already have $P(\theta, m)$
- $\frac{\delta m}{\delta t} = - \frac{\delta V}{\delta \theta}$

**What do we know?**

- How a body's momentum changes across time depends on how the potential energy acts on the body
- As an analogy for the above, imagine the potential energy $V$ as a set of gravitational wells
- Hence, after picking $m$, we change it based on $V$
- $V = - \log P(\theta|D)$ has the same density distribution as $p = P(\theta|D)$
- In other words, the way $V$ acts upon a body emulates the probability densities in $p$
- Hence, sampling a body's position across time based on $V$ is the same as sampling from $p$
- Hence, samples aggregated from $V$ can be used to estimate $p$

---

_How can we use what we know/have available to find what we need?_

Starting with a randomly sampled momentum value, we can use $\frac{\delta m}{\delta t} = - \frac{\delta V}{\delta \theta}$ to update the momentum across time steps and thereby travel along the contours of the negative log-probability of the posterior and sample the next positions in similarly high-probability-mass regions as the initial sample (i.e. initial position). Using these samples, we can estimate the target distribution $p$, i.e. the posterior. It is key to note that, as derived before, $\frac{\delta V}{\delta \theta} = - \frac{\delta \log(P(D|\theta) P(\theta))}{\delta \theta}$, which means the gradient used to update momentum across time steps only depends on what we already know, namely the likelihood $P(D|\theta)$ and the prior $P(\theta)$.

Note that we can make the proposal after a number of iterations for travelling along the above contour using the chosen momentum — chosen based on $P(m)$ — and if we do so, we can get the proposed sample from a similarly high-probability-mass region of the posterior that is also far from the initial sample. This number of iterations (or alternatively, the time for which we allow the algorithm to travel along the contour) can be picked at random to optimise the algorithm's performance in the long run (reference: [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ from London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)).

---

_Hence, we see how HMC allows more efficient exploration of the high-probability-mass region of the posterior, compared to the approaches that explore by diffusing from a starting point over time (e.g. Metropolis-Hastings)._

---

> **Main references**:
>
> - [_Hamiltonian Monte Carlo For Dummies (Statisticians / Pharmacometricians / All)_ by Alan Maloney, **YouTube**](https://www.youtube.com/watch?v=ZGtezhDaSpM)
> - [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ from London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)
> - ["11.9.3. Hamiltonian Monte Carlo" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Notebook**](https://bayesiancomputationbook.com/markdown/chp_11.html#hamiltonian-monte-carlo)

> **Additional reference**: [_The intuition behind the Hamiltonian Monte Carlo algorithm_ by Ben Lambert, **YouTube**](https://www.youtube.com/watch?v=a-wydhEuAm0)

# Algorithm and practical computation
## Essential steps
- Initialise current sample as $\theta_0$
- Sample $m$ from $\text{Normal}(0, \sigma I)$
- Simulate $\theta_i$ and $m_i$ for some amount of time $T$
- Take $\theta_T$ as our new proposed sample
- Use the Metropolis acceptance criterion to accept or reject $\theta_T$

_Why we still need to use the Metropolis acceptance criterion?_ Intuitively, because we can think of HMC as a Metropolis-Hasting algorithm with a better proposal method. But a further numerical justification is that the accept-reject steps help correct for errors introduced by the numerical simulation of the Hamiltonian equations. _Let us explore this numerical justification._ In practice, we can simulate Hamiltonian dynamics only approximately, which means that even if our momentum is well chosen so as to travel along contours of high-probability-mass, the sample (i.e. position) we reach at the end of our simulation may be from a lower-probability-mass region. To correct for this, we make the probability of accepting the new sample proportional to its distance (in terms of its probability-mass region) to the initial sample (i.e. the starting position of the simulation).

> **Reference**: ["11.9.3. Hamiltonian Monte Carlo" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Notebook**](https://bayesiancomputationbook.com/markdown/chp_11.html#hamiltonian-monte-carlo)

---

The above algorithm is essentially two key steps (done for each iteration of HMC):

**Step 1: Obtain a new momentum**:

- A new momentum is randomly drawn from a Gaussian distribution
- The momentum is drawn independently of the current momentum and position

**NOTE**: _The momentum is always drawn anew from a Gaussian distribution every iteration._

 **Step 2: Probabilistically update both position and momentum**:
 
 - New momentum and position are obtained after a number of simulation steps
 - The new position is the new proposed sample
 - Update is "probabilistic" due to the Metropolis acceptance criterion

**NOTE**: _The new momentum and the new position are used to calculate the new Hamiltonian. This is important, because the difference between the previous Hamiltonian and the new Hamiltonian is needed to obtain the acceptance probability when checking the Metropolis acceptance criterion, as we shall see later._

> **Reference**: [_MCMC using Hamiltonian dynamics_ by Radford M. Neal](https://arxiv.org/pdf/1206.1901)

---

**NOTE**: "Simulate" <br>
$\implies$ Simulate the system defined by the Hamiltonian equations <br>
$\implies$ Travelling along the contours as per the momentum

## Metropolis acceptance criterion for HMC
> **Reference**: [_MCMC using Hamiltonian dynamics_ by Radford M. Neal](https://arxiv.org/pdf/1206.1901)

As stated before, we need to use the Metropolis acceptance criterion for two reasons: (1) intuitively, we can think of HMC as a Metropolis-Hasting algorithm with a better proposal method, and (2) as a further numerical justification, the accept-reject steps help correct for errors introduced by the numerical simulation of the Hamiltonian equations.

_But how do we define the Metropolis criterion for HMC?_

Note that in the second essential step of the HMC algorithm, Hamiltonian dynamics are used to propose a new position (i.e. a new sample/state). Starting with the current position and momentum $(\theta, m)$, Hamiltonian dynamics are simulated for a number of steps (e.g. using the Leapfrog method); to be exact, we simulate the trajectory of the point representing the sampler for a number of steps, based on the momenta (as calculated throughout the steps) and the contours of the posterior (or more precisely, the negative log-probability of the posterior). The momentum at the end of this simulated trajectory is then negated (to see why, see the note below), giving a new position and momentum $(\theta^∗, m^*)$. The new, i.e. proposed position $\theta^*$ is accepted as the next state of the Markov chain with probability:

$\min [1, e^{H(\theta, m)−H(\theta^∗, m^∗)}]$, where:

- $H$ is the Hamiltonian, given by $H(\theta, m) = K(m) + V(\theta)$
- $V$ is analogous to the potential energy in classical mechanics
- $K$ is analogous to the kinetic energy in classical mechanics

If the proposed state (i.e. position) is not accepted, the next state is the same as the current state.

---

**Intuition for the above**:

We have the following cases:

1. $e^{H(\theta, m)−H(\theta^∗, m^∗)} \geq 1 \implies H(\theta^∗, m^∗) \geq H(\theta, m)$
2. $e^{H(\theta, m)−H(\theta^∗, m^∗)} \leq 1 \implies H(\theta^∗, m^∗) \leq H(\theta, m)$

$H(\theta^∗, m^∗) \geq H(\theta, m)$ means the proposed state is from an equal or higher-probability-mass region of the posterior, which means it should always be accepted, because we want to sample more from equal or higher-probability-mass regions. $H(\theta^∗, m^∗) < H(\theta, m)$ means the proposed state is from a lower-probability-mass region, which means it should be accepted only probabilistically, with the probability of accepting it being proportional to its closeness to the current state (in terms of probability density), because we want there to be a lower but non-zero chance of sampling from a sparser region region after sampling from a denser region, with the condition that the lower the density, the lower the chance.

---

**NOTE: How do we calculate**  $H(\theta, m) − H(\theta^∗, m^∗)$ **?**

In the case of HMC, the Hamiltonian is given by:

$H(\theta, m) = - \log P(\theta, m) = - \log P(\theta|D) - \log P(m)$

Of course, we do not know $P(\theta|D)$, since this is the target distribution we want to find. However:

$P(\theta|D) \propto P(D|\theta) P(\theta)$

$\implies - \log P(\theta|D) \propto - \log(P(D|\theta) P(\theta)) = - \log P(D|\theta) - \log P(\theta)$

$\implies H(\theta, m) \propto - \log P(D|\theta) - \log P(\theta) - \log P(m)$

Likewise, $H(\theta^*, m^*) \propto - \log P(D|\theta^*) - \log P(\theta^*) - \log P(m^*)$.

The right-hand side in the above two statements is sufficient for our needs. Why? Consider:

Let $P(\theta|D) = \frac{P(D|\theta) P(\theta)}{z}$ for some normalisation constant $z$

$\implies - \log P(\theta|D) = - \log \frac{P(D|\theta) P(\theta)}{z} = - \log P(D|\theta) - \log P(\theta) + \log z$

$\implies H(\theta, m) = - \log P(D|\theta) - \log P(\theta) - \log P(m) + \log z$

Likewise, $H(\theta^*, m^*) = - \log P(D|\theta^*) - \log P(\theta^*) - \log P(m^*) + \log z$

Hence, we get $H(\theta, m) − H(\theta^∗, m^∗)$ as follows:

$- \log P(D|\theta) - \log P(\theta) - \log P(m) + \log z - (- \log P(D|\theta^*) - \log P(\theta^*) - \log P(m^*) + \log z)$

$= - \log P(D|\theta) - \log P(\theta) - \log P(m) + \log z + \log P(D|\theta^*) + \log P(\theta^*) + \log P(m^*) - \log z$

$= - \log P(D|\theta) - \log P(\theta) - \log P(m) + \log P(D|\theta^*) + \log P(\theta^*) + \log P(m^*)$

As we can see, the normalisation constant is eliminated, so it has no effect on the acceptance probability.

---

**NOTE: Why negate the momentum variable after the simulation?**

The negation of the momentum at the end of the simulated trajectory makes the Metropolis proposal symmetrical, as needed for the acceptance probability above to be valid (**NOTE**: _I do not get this point_). However, this negation need not be done in practice, since $K(m) = K(−m)$, and since the momentum is always replaced (by randomly sampling it from a Gaussian) in the first step of the next iteration.

# Additional points about HMC
- HMC is fast and efficient when it works
- HMC is robust, i.e. it works for a wide variety of distributions
- When HMC breaks, it is very obvious to observe and report it <br> $\rightarrow$ _HMC has unique diagnostics for when it is broken_

---

_The above points make HMC a powerful choice to automate Bayesian computation._

---

- HMC does not work well for multimodal distributions
- Adiabatic Monte Carlo extends HMC to work for mutlimodal distributions
- Hamiltonian equations are solved using symplectic integrators

---

> **Reference**: [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ from London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)