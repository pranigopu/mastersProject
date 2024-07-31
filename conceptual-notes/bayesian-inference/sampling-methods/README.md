**SAMPLING METHODS**

---

**Contents**:

- [Introduction to sampling methods from a Bayesian context](#introduction-to-sampling-methods-from-a-bayesian-context)
- [Further reading](#further-reading)
- [Sampling methods not discussed](#sampling-methods-not-discussed)

---

# Introduction to sampling methods from a Bayesian context
Suppose we have a distribution $p$ which we do not yet know fully, but of which we know only the numerator (or more generally, of which we know only some function proportional to it). Note how this situation perfectly matches our situation in many cases of Bayesian inference, where we have the numerator of the posterior distribution but not the denominator, which can be impractical or even impossible to compute (by either estimation or calculation) with enough accuracy. Hence, we see that if we have methods to estimate $p$ using sampling based on some use of the numerator of $p$ to weight the acceptance or rejection of samples, then we shall have methods to at least try to estimate the posterior distribution of a Bayesian model, thereby helping us to perform Bayesian inference in cases where the closed expression of the model cannot be found in its entirety.

# Further reading
- [**1. Markov chain Monte Carlo (MCMC)**](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc)
    - [Metropolis-Hastings (MH)](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc/metropolis-hastings-mh.md)
    - [Hamiltonian Monte Carlo (HMC)](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc/hamiltonian-monte-carlo-hmc.md)
- [**2. Variational Inference**](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/variational-inference-vi)
    - [Bayes-by-Backprop](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/variational-inference-vi/bayes-by-backprop.md)

# Sampling methods not discussed
- Sequential Monte Carlo