**MARKOV CHAIN MONTE CARLO (MCMC)**

---

**Contents**:

- [Motivation](#motivation)
- [Notation](#notation)
- [Key ideas behind MCMC](#key-ideas-behind-mcmc)
- [The driving question of MCMC](#the-driving-question-of-mcmc)
- [Detailed balance condition](#detailed-balance-condition)
- [Key advantange and disadvantage of MCMC](#key-advantange-and-disadvantage-of-mcmc)
- [MCMC vs. multimodal distributions](#mcmc-vs-multimodal-distributions)
- [Key points on MCMC](#key-points-on-mcmc)
- [Further reading: MCMC methods](#further-reading-mcmc-methods)

---

**Abbreviations**:

- MCMC: Markov chain Monte Carlo

---

# Motivation
**_A broad class of sampling methods_**

It forms the theoretical basis for the Metropolis-Hastings algorithm, which is a foundational sampling method.

# Notation
Let $p$ be the target distribution we aim to estimate through samples.


# Key ideas behind MCMC
- When we get a sample with a high probability of being in $p$, we want to tend to take samples from its vicinity <br> _Hence, we can get more high-probability samples and thus estimate_ $p$ _with more confidence and efficiency_
- Hence, we want future samples to depend on past samples in some way
- More specifically, we want the next sample to depend on the previous sample

The last key idea essentially becomes the use of a Markov chain for sampling. Furthermore, we are taking a sequence of random samples from the Markov chain to estimate the target distribution $p$, which is essentially a Monte Carlo simulation used to estimate $p$. Hence, our key ideas lead to the combination of a Markov chain and a Monte Carlo simulation, i.e. it leads to a Markov chain Monte Carlo (MCMC) sampling method.

---

**NOTE 1**: A sample having a high probability of being in the target distribution simply means that it is from a high-probability-mass region of the target distribution. For example, if the target distribution is a normal distribution, samples corresponding to points near the mean are from a higher-probability-mass region than samples corresponding to points further away in the tails; the former have a higher probability of being in the given normal distribution than the latter.

**NOTE 2**: Seeking more higher-probability samples does not preclude the inclusion of lower-probability samples; indeed, for an accurate estimation of the target distribution, we need all kinds of samples. But the proportion of each kind of sample taken corresponds to its probability with respect to the distribution; we want to sample more higher-probability samples in proportion to how relatively high their probabilities are, while sampling lower-probability samples more occasionally, also in proportion to how relatively low their probabilities are.

# The driving question of MCMC
**_How to design a Markov chain that samples from the target distibution?_**

Based on our reliance on random sampling and our reliance on using the probability of a sample being from the target distribution, it stands to reason that we cannot expect to sample from the target distribution to begin with, but we expect to get there eventually. Furthermore, when we get the point where we begin sampling from the target distribution, we expect to the stay there, more or less. Note that here, each "state" in the Markov chain is a sample. Furthermore, note that by the nature of the goal, the Markov chain is not bound to a finite set of states.

Hence, our aim is to design a Markov chain with transition probabilities such that eventually, each sample is drawn from the same distribution as the previous sample, with the distribution here being the target distribution. What it means is that eventually, the probability of drawing a given sample in the next time step from the Markov chain, disregarding the current sample and the current time step, would converge to the probability of drawing it from the target distribution itself.

**NOTE**: _We disregard the current sample and the current time step because we are looking at the long-run probability of drawing the sample._

Now, note that the probability of drawing a given sample in the next time step from the Markov chain, disregarding the current sample and the current time step, is the steady-state probability of the given sample (remember that here, a sample is a state, and drawing the next sample means transitioning to the next state). Hence, we need to design a Markov chain that has steady-state behaviour, wherein its steady-state probabilities represent the target distribution (for more on steady-state behaviour of a Markov chain, see: [_Steady-State Behaviour of Markov Chains_ from **Markov Chains** from `conteptual-notes`](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/markov-chains/steady-state-behaviour-of-markov-chains.md)).

Note that it may take a while for the overall (i.e. long-run) transition probabilities to settle, which means that there would be a sequence of samples (i.e. states) that need to be drawn before we reach the point where the samples tend by-and-large to fit the target distribution. These sequence of samples are the "burn in" samples. The key consideration in designing the right Markov chain is that the transition probabilities between the states (i.e. the samples drawn) lead to the required steady-state probabilities.

# Detailed balance condition
One way to design the required transition probabilities with respect to a given target distribution $p$ (which the steady-state probabilities should represent) is by noting that once the Markov chain has reached the point where the samples are drawn by-and-large from the target distribution, then the long-range (i.e. steady-state) probability of observing a state $x$ (i.e. drawing a sample $x$ in our case) and then transitioning to state $y$ (i.e. then drawing the sample $y$ in our case) should be the same as the long-range (i.e. steady-state) probability of observing $y$ and then transitioning to $x$. Why is this condition valid? Because when the Markov chain has reached the point where the samples are drawn by-and-large from the target distribution, then the joint probability of drawing two samples next-to-next should be independent of the order in which they were drawn. In the context of a Markov chain, it is called the "detailed balance condition". Mathematically, it is as follows:

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

# Key advantange and disadvantage of MCMC
The main disadvantage of MCMC is also its main advantage: in MCMC samples are not uncorrelated, which means that while we are more likely to sample more around samples that have a high-probability of being in the target distribution, the downside is that we may get a biased or incomplete estimate for the target distribution, since our sampling is no longer exactly random and thus may not be representative of the distribution it is drawn from.

# MCMC vs. multimodal distributions
Multimodal distributions where the modes barely overlap typically pose difficulties to MCMC algorithms. This is because exploring them fully requires entering and passing through a region of low probability density which, by the very nature of MCMC, is a rare event (reference: [_Training BNNs with HMC_ from **janosh.dev**](https://janosh.dev/posts/hmc-bnn)). Hamiltonian Monte Carlo (HMC) (see: ["MCMC METHOD 2: Hamiltonian Monte Carlo (HMC)](#mcmc-method-2-hamiltonian-monte-carlo-hmc)) is a class of MCMC methods that aims to overcome this problem.

# Key points on MCMC
- MCMC can be _potentially_ more efficient, but is not necessarily so
- MCMC focuses on sampling more from the higher-probability-mass regions of the target distribution
- However, due to randomness, lower-density regions are also sampled (as they must be, of course), but relatively less
- MCMC is an umbrella term for a wide variety of methods that define how to design the transition probabilities
- The specific acceptance and rejection methods used under the broader MCMC framework define the specific MCMC method

# Further reading: MCMC methods
- [Metropolis-Hastings (MH)](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc/metropolis-hastings-mh.md)
- [Hamiltonian Monte Carlo (HMC)](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc/hamiltonian-monte-carlo-hmc.md)