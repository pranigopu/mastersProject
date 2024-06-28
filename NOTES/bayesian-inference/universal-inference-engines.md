**SAMPLING**

---

**Contents**:

- [Introduction](#introduction)
- [Markov chain Monte Carlo](#markov-chain-monte-carlo)
    - [Key advantange and disadvantage of MCMC](#key-advantage-and-disadvantage-of-mcmc)
    - [Key points about MCMC](#key-points-about-mcmc)

---

# Introduction from a Bayesian context
Suppose we have a distribution $p$ which we do not yet know fully, but which we know only the numerator of. Note how this situation perfectly matches our situation in many cases of Bayesian inference, where we have the numerator of the posterior distribution but not the denominator, which can be impractical or even impossible to compute (by either estimation or calculation) with enough accuracy. Hence, we see that if we have methods to estimate $p$ using sampling based on some use of the numerator of $p$ to weight the acceptance or rejection of samples, then we shall have methods to at least try to estimate the posterior distribution of a Bayesian model, thereby helping us to perform Bayesian inference in cases where the closed expression of the model cannot be found in its entirety.

# Markov chain Monte Carlo
**_A broad sampling method_**

Let $p$ be the target distribution we aim to estimate through samples.

KEY IDEAS:

- When we get a sample with a high probability of being in $p$, we want to take samples from its vicinity <br> _Hence, we can get more high-probability samples and thus estimate_ $p$ _with more confidence and efficiency_
- Hence, we want future samples to depend on past samples in some way
- More specifically, we want the next sample to depend on the previous sample

The last key idea essentially becomes the use of a Markov chain for sampling. Furthermore, we are taking a sequence of random samples from the Markov chain to estimate the target distribution $p$, which is essentially a Monte Carlo simulation used to estimate $p$. Hence, our key ideas lead to the combination of a Markov chain and a Monte Carlo simulation, i.e. it leads to a Markov chain Monte Carlo (MCMC) sampling method.

KEY QUESTION: How to design a Markov chain that samples from the target distibution?

Based on our reliance on random sampling and our reliance on using the probability of a sample being from the target distribution, it stands to reason that we cannot expect to sample from the target distribution to begin with, but we expect to get there eventually. Furthermore, when we get the point where we begin sampling from the target distribution, we expect to the stay there, more or less. Note that here, each "state" in the Markov chain is a sample. Furthermore, note that by the nature of the goal, the Markov chain is not bound to a finite set of states.

Hence, our aim is to design a Markov chain with transition probabilities such that eventually, each sample is drawn from the same distribution as the previous sample, with the distribution here being the target distribution. What it means is that eventually, the probability of drawing a given sample in the next time step from the Markov chain, disregarding the current sample and the current time step, would converge to the probability of drawing it from the target distribution itself. Now, note that the probability of drawing a given sample in the next time step from the Markov chain, disregarding the current sample and the current time step, is the steady-state probability of the given sample (remember that here, a sample is a state, and drawing the next sample means transitioning to the next state). Hence, we need to design a Markov chain that has steady-state behaviour, wherein its steady-state probabilities represent the target distribution.

**NOTE**: _We disregard the current sample and the current time step because we are looking at the long-run probability of drawing the sample._

Note that it may take a while for the overall (i.e. long-run) transition probabilities to settle, which means that there would be a sequence of samples (i.e. states) that need to be drawn before we reach the point where the samples tend by-and-large to fit the target distribution. These sequence of samples are the "burn in" samples. The key consideration in designing the right Markov chain is that the transition probabilities between the states (i.e. the samples drawin) lead to the required steady-state probabilities.

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

## Key points about MCMC
- MCMC can be _potentially_ more efficient, but is not necessarily so
- MCMC focuses on sampling more from the higher-density regions of the target distribution
- However, due to randomness, lower-density regions are also sampled (as they must be, of course), but relatively less
- MCMC is an umbrella term for a wide variety of methods that define how to design the transition probabilities
- The specific acceptance and rejection methods used under the broader MCMC framework define the specific MCMC method

# Metropolis-Hastings algorithm
**_An MCMC method_**

Let $f$ represent the numerator of the target distribution $p$.

## Defining the transition probability
The transition probability is made of two components...

**1. Sampling probability**:

The next sample is sampled based on the current sample using an easier distribution $g$ whose parameters depend on the current sample. For example, we can define the probability of sampling $b$ given the current sample $a$ based on the distribution defined as $g(b | a) = \text{Normal}(a, \sigma^2)$.

**2. Acceptance probability**:

The next sample drawn based on the current sample is accepted or rejected based on the acceptance probability $A$. This is essentially the transition probability from the current state $a$ to the next state $b$ given that $b$ is what has been sampled after $a$ according to the sampling probability $g(b | a)$. It is denoted by $A(a \rightarrow b)$, read as "the probability of accepting the move from the sample $a$ to the proposed sample $b$".

---

Hence, the transition probability of going from state $a$ (i.e. sampling $a$) to state $b$ (i.e. sampling $b$) is the probability of sampling $b$ after $a$ and then accepting $b$. Mathematically, it is given by:

$g(b | a) A(a \rightarrow b)$.


How should the acceptance probability a.k.a. the transition probability $A$ be defined? Here, we use the detailed balance condition seen in MCMC (see: ["Detailed balance condition" from "Markov chain Monte Carlo"](#detailed-balance-condition), which is given by the following (note that $\Theta$ is the sample space):

$p(x) A(y|x) = p(y) A(x|y) \text{ } \forall x \in \Theta,  \text{ } \forall y \in \Theta$


