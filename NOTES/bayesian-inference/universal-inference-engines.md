**UNIVERSAL INFERENCE ENGINE**

---

**Contents**:

---

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
