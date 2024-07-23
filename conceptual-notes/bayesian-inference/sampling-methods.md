**SAMPLING METHODS**

---

**Contents**:

- [Introduction from a Bayesian context](#introduction-from-a-bayesian-context)
- [Markov chain Monte Carlo (MCMC)](#markov-chain-monte-carlo-mcmc)
  - [Detailed balance condition](#detailed-balance-condition)
  - [Key advantange and disadvantage of MCMC](#key-advantange-and-disadvantage-of-mcmc)
  - [Key points](#key-points)
  - [MCMC METHOD 1: Metropolis-Hastings](#mcmc-method-1-metropolis-hastings)
    - [Defining the transition probability](#defining-the-transition-probability)
    - [Defining the acceptance probability](#defining-the-acceptance-probability)
    - [Metropolis algorithm](#metropolis-algorithm)
  - [MCMC METHOD 2: Hamiltonian Monte Carlo (HMC)](#mcmc-method-2-hamiltonian-monte-carlo-hmc)
    - [Key concepts](#key-concepts)
      - [Momentum](#momentum)
      - [Hamiltonian (i.e. Hamiltonian function)](#hamiltonian-ie-hamiltonian-function)
    - [Mathematical formulation](#mathematical-formulation)
    - [Algorithm and practical computation](#algorithm-and-practical-computation)
    - [Additional points about HMC](#additional-points-about-hmc)
- [Variational inference (VI)](#variational-inference-vi)
  - [Motivation](#motivation)
  - [Conceptual introduction](#conceptual-introduction)
  - [Theoretical foundations](#theoretical-foundations)
  - [Practical computation](#practical-computation)
    - [Introduction](#introduction)
    - [Bayes-by-backprop](#bayes-by-backprop)
- [Other sampling methods](#other-sampling-methods)

---

# Introduction from a Bayesian context
Suppose we have a distribution $p$ which we do not yet know fully, but of which we know only the numerator (or more generally, of which we know only some function proportional to it). Note how this situation perfectly matches our situation in many cases of Bayesian inference, where we have the numerator of the posterior distribution but not the denominator, which can be impractical or even impossible to compute (by either estimation or calculation) with enough accuracy. Hence, we see that if we have methods to estimate $p$ using sampling based on some use of the numerator of $p$ to weight the acceptance or rejection of samples, then we shall have methods to at least try to estimate the posterior distribution of a Bayesian model, thereby helping us to perform Bayesian inference in cases where the closed expression of the model cannot be found in its entirety.

# Markov chain Monte Carlo (MCMC)
**_A broad sampling method_**

**MOTIVATION**: Why is it important?

It forms the theoretical basis for the Metropolis-Hastings algorithm, which is a foundational sampling method.

---

**NOTATION**:

Let $p$ be the target distribution we aim to estimate through samples.

---

KEY IDEAS:

- When we get a sample with a high probability of being in $p$, we want to tend to take samples from its vicinity <br> _Hence, we can get more high-probability samples and thus estimate_ $p$ _with more confidence and efficiency_
- Hence, we want future samples to depend on past samples in some way
- More specifically, we want the next sample to depend on the previous sample

The last key idea essentially becomes the use of a Markov chain for sampling. Furthermore, we are taking a sequence of random samples from the Markov chain to estimate the target distribution $p$, which is essentially a Monte Carlo simulation used to estimate $p$. Hence, our key ideas lead to the combination of a Markov chain and a Monte Carlo simulation, i.e. it leads to a Markov chain Monte Carlo (MCMC) sampling method.

---

**NOTE 1**: A sample having a high probability of being in the target distribution simply means that it is from a high-probability-mass region of the target distribution. For example, if the target distribution is a normal distribution, samples corresponding to points near the mean are from a higher-probability-mass region than samples corresponding to points further away in the tails; the former have a higher probability of being in the given normal distribution than the latter.

**NOTE 2**: Seeking more higher-probability samples does not preclude the inclusion of lower-probability samples; indeed, for an accurate estimation of the target distribution, we need all kinds of samples. But the proportion of each kind of sample taken corresponds to its probability with respect to the distribution; we want to sample more higher-probability samples in proportion to how relatively high their probabilities are, while sampling lower-probability samples more occasionally, also in proportion to how relatively low their probabilities are.

---

KEY QUESTION: How to design a Markov chain that samples from the target distibution?

Based on our reliance on random sampling and our reliance on using the probability of a sample being from the target distribution, it stands to reason that we cannot expect to sample from the target distribution to begin with, but we expect to get there eventually. Furthermore, when we get the point where we begin sampling from the target distribution, we expect to the stay there, more or less. Note that here, each "state" in the Markov chain is a sample. Furthermore, note that by the nature of the goal, the Markov chain is not bound to a finite set of states.

Hence, our aim is to design a Markov chain with transition probabilities such that eventually, each sample is drawn from the same distribution as the previous sample, with the distribution here being the target distribution. What it means is that eventually, the probability of drawing a given sample in the next time step from the Markov chain, disregarding the current sample and the current time step, would converge to the probability of drawing it from the target distribution itself.

Now, note that the probability of drawing a given sample in the next time step from the Markov chain, disregarding the current sample and the current time step, is the steady-state probability of the given sample (remember that here, a sample is a state, and drawing the next sample means transitioning to the next state). Hence, we need to design a Markov chain that has steady-state behaviour, wherein its steady-state probabilities represent the target distribution.

**NOTE**: _We disregard the current sample and the current time step because we are looking at the long-run probability of drawing the sample._

Note that it may take a while for the overall (i.e. long-run) transition probabilities to settle, which means that there would be a sequence of samples (i.e. states) that need to be drawn before we reach the point where the samples tend by-and-large to fit the target distribution. These sequence of samples are the "burn in" samples. The key consideration in designing the right Markov chain is that the transition probabilities between the states (i.e. the samples drawn) lead to the required steady-state probabilities.

## Detailed balance condition
One way to design the required transition probabilities with respect to a given target distribution $p$ (which the steady-state probabilities should represent) is by noting that once the Markov chain has reached the point where the samples are drawn by-and-large from the target distribution, then the long-range (i.e. steady-state) probability of observing a state $x$ (i.e. drawing a sample $x$ in our case) and then transitioning to state $y$ (i.e. then drawing the sample $y$) should be the same as the long-range (i.e. steady-state) probability of observing $y$ and then transitioning to $x$. Why is the condition valid? Because when the Markov chain has reached the point where the samples are drawn by-and-large from the target distribution, then the joint probability of drawing two samples next-to-next should be independent of the order in which they were drawn. In the context of a Markov chain, it is called the "detailed balance condition". Mathematically, it is as follows:

$p(x) T(y|x) = p(y) T(x|y) \text{ } \forall x \in \Theta,  \text{ } \forall y \in \Theta$

Here:

- $T(u|v)$ is the transition probability from state $v$ to state $u$
- $p$ is the steady-state probability distribution, which is meant to equal the target distribution
- $\Theta$ is the sample space

---

We can see that the above condition implies that $p$ is a stationary distribution because:

- $\displaystyle p(y) = \sum_{x \in \Theta} p(x) T(y|x)$
- $\displaystyle p(x) = \sum_{y \in \Theta} p(y) T(x|y)$

In other terms, the total probability of transitioning from some random state to a given state is the same as observing the given state, disregarding the current state and current time step. In other words, the overall probability distribution does not change between transitions, showing a steady-state behaviour and hence a stationary distribution.

## Key advantange and disadvantage of MCMC
The main disadvantage of MCMC is also its main advantage: in MCMC samples are not uncorrelated, which means that while we are more likely to sample more around samples that have a high-probability of being in the target distribution, the downside is that we may get a biased or incomplete estimate for the target distribution, since our sampling is no longer exactly random and thus may not be representative of the distribution it is drawn from.

## Key points
- MCMC can be _potentially_ more efficient, but is not necessarily so
- MCMC focuses on sampling more from the higher-probability-mass regions of the target distribution
- However, due to randomness, lower-density regions are also sampled (as they must be, of course), but relatively less
- MCMC is an umbrella term for a wide variety of methods that define how to design the transition probabilities
- The specific acceptance and rejection methods used under the broader MCMC framework define the specific MCMC method

## MCMC METHOD 1: Metropolis-Hastings
**_An MCMC method_**

**MOTIVATION**: Why is it important?

MH is not a very modern or particularly efficient algorithm, but it is simple to understand and also provides a foundation to understand more sophisticated and powerful methods for sampling from and estimating the posterior distribution (paraphrased from ["1.2. A DIY Sampler, Do Not Try This at Home" from "1. Bayesian Inference" from _Bayesian Modeling and Computation in Python_](https://bayesiancomputationbook.com/markdown/chp_01.html)).

**NOTE**: _MH represents a class of methods, rather than a single method._

---

**NOTATION**:

- Let $f$ represent some function proportional to the target distribution $p$
- Let $g$ be the candidate distribution using which we shall take new samples

**NOTE**: _Commonly,_ $f$ _is the known numerator of_ $p$, _as in the case of_ $p$ _being the posterior in the context of Bayesian inference._

### Defining the transition probability
The transition probability is made of two components...

**1. Sampling probability**:

The next sample is sampled based on the current sample using an easier distribution $g$ whose parameters depend on the current sample. For example, we can define the probability of sampling $b$ given the current sample $a$ based on the distribution defined as $g(b | a) = \text{Normal}(a, \sigma^2)$.

**2. Acceptance probability**:

The next sample drawn based on the current sample is accepted or rejected based on the acceptance probability $A$. This is essentially the transition probability from the current state $a$ to the next state $b$ given that $b$ is what has been sampled after $a$ according to the sampling probability $g(b|a)$. It is denoted by $A(a \rightarrow b)$, read as "the probability of accepting the move from the sample $a$ to the proposed sample $b$".

---

Hence, the transition probability of going from state $a$ (i.e. sampling $a$) to state $b$ (i.e. sampling $b$) is the probability of sampling $b$ after $a$ and then accepting $b$. Mathematically, it is given by: $g(b|a) A(a \rightarrow b)$

### Defining the acceptance probability
How should the acceptance probability a.k.a. the transition probability $A$ be defined? Here, we use the detailed balance condition seen in MCMC (see: ["Detailed balance condition" from "Markov chain Monte Carlo"](#detailed-balance-condition)). Let $T(u|v)$ be the transition probability from state $v$ to state $u$, and let $\Theta$ be the sample space. Then, by the detailed balance condition:

$p(a) T(b|a) = p(b) T(a|b) \text{ } \forall a \in \Theta,  \text{ } \forall b \in \Theta$

We know that $f$ is proportional to $p$. Let $p(x) = \frac{f(x)}{N}$, for some $N$. Then:

$\frac{f(x)}{N} g(b|a) A(a \rightarrow b) = \frac{f(x)}{N} g(a|b) A(b \rightarrow a)$

$\implies \frac{A(a \rightarrow b)}{A(b \rightarrow a)} = \frac{f(a)}{f(b)} \frac{g(a|b)}{g(b|a)}$

---

For convenience, put $\frac{f(a)}{f(b)} = r_f$ and $\frac{g(a|b)}{g(b|a)} = r_g$. Then:

$\frac{A(a \rightarrow b)}{A(b \rightarrow a)} = r_f r_g$

Now, given that we know $A$ defines a probability, we know that $A(a \rightarrow b) \leq 1$ and $A(b \rightarrow a) \leq 1$.

---

Using the above inequalities and equation, we get the following cases:

1. $r_f r_g < 1 \implies A(a \rightarrow b) = r_f r_g$ and $A(b \rightarrow a) = 1$
2. $r_f r_g \geq 1 \implies A(a \rightarrow b) = 1$ and $A(b \rightarrow a) = \frac{1}{r_f r_g}$

We can simplify the above cases as follows:

$A(a \rightarrow b) = \max(1, r_f r_g)$

---

**INTUITION FOR THE ABOVE**:

For simplicity, let us assume $g$ is symmetrical, i.e. $g(a|b) = g(b|a)$. Hence:

$\frac{A(a \rightarrow b)}{A(b \rightarrow a)} = \frac{f(b)}{f(a)} \frac{g(a|b)}{g(b|a)} = \frac{f(a)}{f(b)}$

Hence, we have that:

$A(a \rightarrow b) = \max(1, r_f r_g) = \max(1, r_f) = \max(1, \frac{f(b)}{f(a)})$

Now, note that $p(x) = \frac{f(x)}{N}$, for some $N$. Hence:

$A(a \rightarrow b) = \max(1, \frac{f(b)}{f(a)}) = \max(1, \frac{p(b)}{p(a)})$

Hence, we have the following cases:

1. $p(b) > p(a) \implies A(a \rightarrow b) = 1$
2. $p(b) < p(a) \implies A(a \rightarrow b) = \frac{p(b)}{p(a)}$

What does this mean, practically? It means that if $b$ is a sample from a higher-probability-mass region of the target distribution $p$ than $a$, then it will certainly be accepted, which makes sense because we want to sample more from higher-probability-mass regions. However, if $b$ is a sample from a lower-density region of the target distribution $p$ than $a$, then it may or may not be accepted from $a$. Furthermore, we see that the probability of accepting $b$ from $a$ is lesser the lesser the density of $b$ is compared to the density of $a$, which also makes sense because we want there to be a lower but non-zero chance of sampling from a lower-density region after sampling from a higher-probability-mass region, with the condition that the lower the density, the lower the chance. We see how such a policy is an MCMC method that helps estimate the target distribution more accurately and more efficiently over time.

### Metropolis algorithm
- The Metropolis algorithm is a special case of MH
- In Metropolis, the candidate distribution $g$ is strictly symmetrical
- On the other hand, MH can have an asymmetrical candidate distribution as well

## MCMC METHOD 2: Hamiltonian Monte Carlo (HMC)
**NOTE**: _HMC is a class of methods, rather than a single method._

---

**MOTIVATION**: Why is it important?

HMC is a class of MCMC methods that uses gradients (of the log-probability of the posterior distribution) to generate new proposed states (i.e. new samples proposed to be from the target distribution). The gradients of the log-probability of the posterior evaluated at a given state (i.e. a given sample) gives information about the posterior density function's geometry. HMC tries to avoid the random walk behavior typical of Metropolis-Hastings by using the gradient to propose new positions (i.e. new samples) that is both far from the current position (i.e. current sample) and with high acceptance probability. This allows HMC to better scale to higher dimensions and, in principle, to more complex geometries (compared to alternative methods). Intuitively, we can think of HMC as a Metropolis-Hasting algorithm with a better sample proposal distribution.

**NOTE**: _The benefit of consistently proposing new positions that are both far from the current position and with high acceptance rate is that you are likely to gain a much more representative and thus accurate sample of the distribution you want to estimate, but using fewer sampled values; in other words, it tends to make sampling more efficient._

**REMINDER**: _A "sample" here is a tuple of one or more values proposed parameter values of the target distribution. What we are trying to do, here and in all sampling methods, is discover (with some level of uncertainty) how well the various potential parameter values would describe the target distribution. Note also that a "position" or a "state" is simply a sample, i.e. simply a proposed tuple of parameter values._

---

**NOTATION**:

- Let $p$ denote the target distribution
- Let $\theta$ denote a particular position (i.e. state/sample)
- Let $m$ denote the "momentum" parameter (to be defined soon)
- Let $D$ denote the observed data

### Key concepts
#### Momentum
$m$ , i.e. the "momentum", denotes a parameter used to alter how the Markov chian moves along the gradients (i.e. along the shape of the function corresponding to an approximation of the posterior) to the next state/sample. Why would alter such movement? Because we are not interested in following the gradient toward the mode (i.e. the peak, i.e. the hill, i.e. the local optimum), but rather, we are interested in exploring the high-probability-mass region of the posterior. _How high is high enough? Depends on our purposes_.

The analogy commonly used to describe HMC is based on classical mechanics. Let us use the analogy of a planet whose centre is the mode, with its gravitational pull forming a field of force vectors leading into the centre. Our goal is not to follow the force vectors toward the centre, but rather, our goal is to explore the space around the planet where the gravity is high enough (with respect to our purposes). In cases with multiple models (i.e. multimodal posteriors), we can think of a space with multiple planets fixed in place while each exerts its own gravitational pull.

"Momentum" in the context of HMC is analogous to the physical momentum given to a body in space so that it follows a certain orbital trajectory rather than a trajectory that goes directly toward the planet's centre. More precisely, it is an auxiliary variable that ensures that the Markov chain sampling (done based on following the gradient) samples from a sufficiently high-probability-mass region of the posterior rather than moving toward the posterior distribution's mode.

**NOTE**: _Momentum is a vector quantity and can be multi-dimensional. A one-dimensional momentum (a single value) is the momentum of a body along a line, a two-dimensional momentum (a vector of two values) is the momentum of a body across a plane, a three-dimensional momentum (a vector of three values) is the momentum of a body across a space, etc._

---

> **Reference (especially for the analogy**): [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ by London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)

#### Hamiltonian (i.e. Hamiltonian function)
**Preliminary topic: Hamilton's equations of motion**:

This is a function based on the Hamilton's equations of motion (see: ["14.3: Hamilton's Equations of Motion" from _Hamiltonian Mechanics_ from _Classical Mechanics (Tatum)_ from **Classical Mechanics**, **LibreTexts Physics**](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Classical_Mechanics_(Tatum)/14%3A_Hamiltonian_Mechanics/14.03%3A_Hamilton%27s_Equations_of_Motion)), which describe the state of a physical system with one body of a fixed mass moving in a space of $n$ dimensions ($n \geq 1$). In essence, Hamilton's equations of motion describe any system's temporal evolution that can be defined with a Hamiltonian function, signifying the total energy of the system.

---

**NOTE 1**: Hamilton's equations of motion only consider the motion of a single body, and do not explicitly take into account interactions with another body or with a surface. However, interactions with other bodies can be described using changes in momentum. Hence, we can take into account interactions (e.g. collisions, gravitational force, a force field, etc.) as functions of the momentum. In the context of HMC, the "body" would be the imaginary point of the sampler, with two kinds of forces being exerted on it: an imaginary momentum and the contours of the posterior distribution.

**NOTE 2**: Hamilton's equations of motion can apply for any number of dimensions, even though in physics, we would only deal with three dimensions. Hence, in a multidimensional function, e.g. a posterior distribution of the parameters of a neural network, Hamilton's equations would still apply despite the high dimensionality of the space.

**NOTE 3**: Even though Hamilton's equations were meant to deal with physical spaces, we can accurately extend their application to analogous simulated or abstract spaces, such as a high-dimensional sample space for the values of a model's parameters. Hence, they provide a valid basis for exploring the posterior distribution and sampling from it more diversely and efficiently.

**Main topic: Hamiltonian function**:

Consider a system $S$ of $k$ dimensions with coordinates $\theta_1, \theta_2 ... \theta_k$ and dimension-specific momenta $m_1, m_2 ... m_k$ (i.e. each coordinate $\theta_i$ is associated with the momentum $m_i$). Let $\theta$ be the position defined by the $k$ coordinates, and let $m$ be the generalised momentum of the body at $\theta$. Hamilton's equations are derived from a function of the position $\theta$ and the generalised momentum $m$. This function is known as the Hamiltonian. The Hamiltonian, represented by $H(\theta, m)$, amounts to the total energy of the system $S$. Note that we assume that the system is self-contained, and hence, that the system's total energy is constant. Hence, $H(\theta, m)$ is constant, even as the positions and momenta change. More precisely, we have that:

$H(\theta, m) = K(\theta) + V(\theta) =$ _constant_

Here:

- $K(m)$: System's total kinetic energy (independent of positions)
- $V(\theta)$: System's total potential energy (independent of momenta)

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

Hence, solving the above equations, we can simulate the system $S$; for example, given the initial position $\theta$ and initial momentum $m$, we can figure out the change in the position and momentum across time. Hence, using Hamilton's equations of motion in such a way, and using our knowledge of the forces acting on the body (describable as functions of the momentum), we can figure out how the body in the system would move over time. In the case of using Hamilton's equations of motion for sampling from a posterior, the forces are an imaginary momentum and the contours of the posterior distribution, both acting upon an imaginary point representing the sampler.

**NOTE**: _The "forces" described in the context of HMC are meant to guide the efficient exploration of the posterior distribution. The contours of the posterior are a given, so the only thing we can tweak to improve the sampler's performance is the momentum, which can be chosen by us._

---

> **References**:
>
> - [_Hamiltonian Monte Carlo For Dummies (Statisticians / Pharmacometricians / All)_ by Alan Maloney, **YouTube**](https://www.youtube.com/watch?v=ZGtezhDaSpM)
> - [_Hamilton's Equations of Motion_ from **StudySmarter.co.uk**](https://www.studysmarter.co.uk/explanations/physics/classical-mechanics/hamiltons-equations-of-motion)

### Mathematical formulation
Let us first define the following:

- $P$, the probability density or mass (depending on context)
- The target distribution $p = P(\theta|D)$ (the posterior distribution)
- $m$, the set of momentum values corresponding to positions $\theta$
- $P(m)$, the model distributing potential sets of momentum values

**NOTE**: _"Position" in this context refer to "sample"._

---

Hence, we have the following joint probability:

$P(\theta, m) = P(\theta|D) P(m)$

$\implies \log P(\theta, m) = \log (P(\theta|D) P(m)) = \log P(\theta|D) + \log P(m)$

$\implies - \log P(\theta, m) = - \log P(\theta|D) - \log P(m)$

---

Notice that the above equation is in the form of a Hamiltonian, where:

- $H(\theta, m) = - \log P(\theta, m)$
- $K(m) = - \log P(m)$ ("kinetic energy")
- $V(\theta) = - \log P(\theta|D)$ ("potential energy")

Note that the logarithms of probabilities are always less than or equal to 0, since probabilities are always between 0 and 1. Hence, negative logarithms of probabilities are always greater than or equal to 0. Hence, the motion-based analogy is valid, which also means that Hamilton's equations of motion will work as intended, i.e. in the same as they do for physical systems.

_What does this mean in practice?_

It means we can use one of Hamilton's equations, i.e. $\frac{d \theta}{dt} = \frac{\delta H}{\delta m}$, to travel along the contours of the negative log-probability of the posterior to propose the next sample (i.e. the next $\theta$) which is in a similarly high-probability-mass region of the posterior as the current sample (i.e. the current $\theta$). Note that we can make the proposal after a number of iterations for travelling along the above contour using the chosen sets of momenta (chosen based on $P(m)$ ), and if we do so, we can get the proposed sample from a similarly high-probability-mass region of the posterior that is also far from the current sample. This number of iterations (or alternatively, the time for which we allow the algorithm to travel along the contour) can be picked at random to optimise the algorithm's performance in the long run (reference: [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ from London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)).

_Hence, we see how HMC allows more efficient exploration of the high-probability-mass region of the posterior, compared to the approaches that explore by diffusing from a starting point over time._

---

> **Main references**:
>
> - [_Hamiltonian Monte Carlo For Dummies (Statisticians / Pharmacometricians / All)_ by Alan Maloney, **YouTube**](https://www.youtube.com/watch?v=ZGtezhDaSpM)
> - [_Michael Betancourt: Scalable Bayesian Inference with Hamiltonian Monte Carlo_ from London Machine Learning Meetup, **YouTube**](https://www.youtube.com/watch?v=jUSZboSq1zg)
> - ["11.9.3. Hamiltonian Monte Carlo" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Notebook**](https://bayesiancomputationbook.com/markdown/chp_11.html#hamiltonian-monte-carlo)

> **Additional reference**: [_The intuition behind the Hamiltonian Monte Carlo algorithm_ by Ben Lambert, **YouTube**](https://www.youtube.com/watch?v=a-wydhEuAm0)

### Algorithm and practical computation
- Initialise current sample as $\theta_0$
- Sample $m$ from $\text{Normal}(0, \sigma I)$
- Simulate $\theta_i$ and $m_i$ for some amount of time $T$
- Take $\theta_T$ as our new proposed sample
- Use the Metropolis acceptance criterion to accept or reject $\theta_T$

> **Reference**: ["11.9.3. Hamiltonian Monte Carlo" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Notebook**](https://bayesiancomputationbook.com/markdown/chp_11.html#hamiltonian-monte-carlo)

---

**NOTE**: "Simulate" <br>
$\implies$ Simulate the system defined by the Hamiltonian equations <br>
$\implies$ Travelling along the contours as per the momenta

---

Why we still need to use the Metropolis acceptance criterion? Intuitively, because we can think of HMC as a Metropolis-Hasting algorithm with a better proposal method. But a further numerical justification is that the accept-reject steps help correct for errors introduced by the numerical simulation of the Hamiltonian equations.

### Additional points about HMC
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

# Variational inference (VI)
> **Main resources**:
>
> - [_Hands-on Bayesian Neural Networks – A Tutorial for Deep Learning Users_](https://arxiv.org/pdf/2007.06823)
> - ["11.9.5. Variational Inference" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Book**](https://bayesiancomputationbook.com/markdown/chp_11.html#variational-inference)

## Motivation
MCMC algorithms are the best tools for sampling from the exact posterior. However, their lack of scalability has made them less popular for BNNs, given the size of the models under consideration. Compared to MCMC, variational inference tends to be easier to scale to large data and is faster to run computationally, but with less theoretical guarantees of convergence.

## Conceptual introduction
Variational inference is not an exact method. Rather than allowing sampling from the exact posterior, the idea is to have a distribution $q_\phi(\theta)$, called the variational distribution, parametrized by a set of parameters $\phi$. The values of the parameters $\phi$ are then learned such that the variational distribution $q_\phi(\theta)$ is as close as possible to the exact posterior $p(\theta|D)$. The measure of closeness that is commonly used is the Kullback-Leibler divergence (KL-divergence). In practice we usually choose $q$ to be of simpler form than $p$, and we find the member of $q$'s family of distributions that is the closest to the target distribution $p$ (the closeness being commonly measured by the KL divergence), using optimization.

## Theoretical foundations
**NOTATION**:

$\Theta$ denotes the entire hypothesis space. $E$ denotes "expectation" (computed by the theoretical mean). $E_\theta$ denotes marginal expectation with respect to $\theta$. Note that marginal expectation with respect to $\theta$ is the expectation where everything apart from $H$ is kept constant (i.e. $\theta$, which represents the hypothesised model, is kept variable, while $D$, which represents the observed data, is kept constant).

**NOTE**: _The goal is to minimise the KL-divergence._

---

KL-divergence between $p$ and $q$ is given by:

$KL(q_\phi(\theta) || p(\theta|D))$

$= E_\theta(\log q_\phi(\theta) - \log p(\theta|D))$

$\displaystyle = E_\theta(\log \frac{q_\phi(\theta)}{p(\theta|D)})$

$\displaystyle = \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta)}{p(\theta|D)} d\theta$

---

Now, note that:

$p(\theta, D) = p(\theta|D) p(D)$

$\displaystyle \implies p(\theta|D) = \frac{p(\theta, D)}{p(D)}$

---

Hence, we have that:

$KL(q_\phi(\theta) || p(\theta|D))$

$\displaystyle = \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta) p(D)}{p(\theta, D)} d\theta$

$\displaystyle = p(D) \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta)}{p(\theta, D)} d\theta$

---

Now, note that $p(D)$ is constant with respect to $q_\phi(\theta)$.

Hence, here, $p(D)$ is irrelevant in minimising the KL-divergence.

Hence, here, minimising the KL-divergence means minimising:

$\displaystyle \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta)}{p(\theta, D)} d\theta$

$\displaystyle = E_\theta(\log \frac{q_\phi(\theta)}{p(\theta, D)})$

$= E_\theta(\log q_\phi(\theta) - \log p(\theta, D))$

$= E_\theta(\log q_\phi(\theta)) - E_\theta(\log p(\theta, D))$

---

Minimising the above is the same as maximising the following:

$E_\theta(\log p(\theta, D)) - E_\theta(\log q_\phi(\theta))$

$= E_\theta(\log p(\theta, D) - \log q_\phi(\theta))$

$\displaystyle = E_\theta(\log \frac{p(\theta, D)}{q_\phi(\theta)})$

$\displaystyle = \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{p(\theta, D)}{q_\phi(\theta)} d\theta$

The above is called the evidence lower bound, i.e. **ELBO**. The ELBO is easier to compute, and maximising the ELBO achieves the same optimisation as minimising the KL-divergence. Of course, the last integral above must be computed, and practically, it is usually computed through approximate methods, such as averaging Monte Carlo samples drawn from the surrogate distribution $q_\phi(\theta)$ and plugging them into the ELBO formula.

## Practical computation
### Introduction
Note that VI presents a machine learning optimisation problem, where we have a set of one or more parameters, namely $\phi$ (that defines the approximated posterior $q_\phi$), and an objective function, namely ELBO. The most popular method to optimise the ELBO is stochastic VI (SVI), which is in fact the stochastic gradient descent method applied to VI. Now, note that while VI offers a good mathematical tool for Bayesian inference, it needs to be adapted to deep learning. The main problem is that stochasticity stops backpropagation from functioning at the internal nodes of a network. Solutions to mitigate this problem include:

- Probabilistic backpropagation
- Bayes-by-backprop (_our next main focus_)

### Bayes-by-backprop
**_"backprop" means "backpropagation"_**

> **Main references**:
>
> - [_Bayes by Backprop_ from **Probabilitistic Deep Learning**](https://medium.com/neuralspace/probabilistic-deep-learning-bayes-by-backprop-c4a3de0d9743)

**NOTE**: _The following is my best attempt at understanding Bayes-by-backprop._

Bayes-by-backprop is a practical implementation of SVI combined with a reparametrisation trick to ensure backpropagation works as usual. The first key idea is to use $\epsilon \sim r(\epsilon)$ as a source of noise, wherein the distribution $r$ does not vary. The next key idea is to sample the model parameters $\theta$ not from the approximated posterior $q_{\phi}$ (which is a stochastic function) but from $t(\epsilon, \phi)$ (which is a deterministic function, with only the variable input $\epsilon$ being stochastic). Hence, $\theta \sim t(\epsilon, \phi)$. But the key point here is that $t$ must be defined such that $\theta$ (as sampled from $t$) follows $q_{\phi}$. Note also that $\epsilon$ is independent of $\phi$, which means during backpropagation, it can be considered constant, and its stochasticity does not affect the backpropagation process.

---

**Bayes-by-backprop algorithm**

- $\phi = \phi_0$
- **for** $i=0$ to N do
    - Draw $\epsilon \sim q(\epsilon)$
    - $\theta = t(\epsilon, \phi)$
    - $f(\theta, \phi) = log(q\phi(\theta)) − log(p(D_y | D_x, \theta) p(\theta))$
    - $\Delta_\phi f = \text{backprop}_\phi(f)$
    - $\phi = \phi − \alpha \Delta_\phi f$
- **end for**

---

**NOTATION NOTES**:

- $f$: The objective function
- $\Delta_\phi$: Change with respect to change in $\phi$
- $D_x$: The training inputs
- $D_y$: The training labels

# Other sampling methods
- Sequential Monte Carlo