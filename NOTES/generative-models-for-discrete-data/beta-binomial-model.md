**BETA-BINOMIAL MODEL**

---

**Contents**:

- [Abbreviations](#abbreviations)
- [Key definitions](#key-definitions)
- [Introduction](#introduction)
- [Components of Bayesian inference w.r.t. beta-binomial model](#components-of-bayesian-inference-wrt-beta-binomial-model)
  - [Defining likelihood](#defining-likelihood)
  - [Defining prior](#defining-prior)
  - [Defining posterior](#defining-posterior)
- [Maximum a posteriori (MAP) estimate of best hypothesis](#maximum-a-posteriori-map-estimate-of-best-hypothesis)
- [Posterior predictive distribution (PPD)](#posterior-predictive-distribution-ppd)
- [Overfitting](#overfitting)

---

# Abbreviations
- **PDF**: Probability density function
- **IID**: Independently and identically distributed

# Key definitions

- **Hypothesis**: A tuple of parameters corresponding to probability distributions proposed to explain given data
- **Hypothesis space**: Set of all hypotheses being considered to explain given data
- **Likelohood**: Probability of observing certain data given a certain hypothesis is true
- **Prior**: Probability of a certain hypothesis being true prior to any observations
- **Posterior**: Probability of a certain hypothesis being true having observed certain data

# Introduction
In many applications we have a multidimensional hypothesis space with continuous values, i.e. hypothesis space $H \subseteq \mathbb{R}^k$, i.e. each hypothesis is a tuple of $k$ real-valued parameters. This is because each hypothesis represents a particular set of probability distributions for the likelihood and prior out of a family of probability distributions. Here, the mathematics is naturally more complex, since we must use integration instead of summation to get the posterior predictive distribution with respect to all the hypotheses.

In beta-binomial models in particular, we take the likelihood as distributed by a binomial distributions and the prior as distributed by a beta distribution. It is a useful model for the following reasons: (1) A prior distributed by a beta distribution is a conjugate prior to a likelihood distributed by a binomial distribution, which means the posterior can be obtained analytically as a beta distribution too. (2) It forms the basis for naive Bayes classifiers and Markov models. (3) It is an easy example to chew on and thereby grasp the broader concepts.

# Components of Bayesian inference w.r.t. beta-binomial model
## Defining likelihood
KEY INTUITION: Avoid suspicious coincidences.

KEY ASSUMPTION: Assume examples are sampled uniformly at random from a particular beta-binomial model

Consider the basic random process of a coin toss. Here, we do not specify the coin as fair, instead giving it a $\theta$ probability of getting heads. Let us focus on getting heads, which means we define the probability of getting heads as the probability of success. Note that the probability of success represents a particular model, given the general idea of a "coin toss" model. Now, consider there to be a fixed number of trials $n$. From here, we can have two kinds of datasets...

**CASE 1: Dataset being a particular sequence of heads and tails**:

$\mathbb{P}(D | \theta) = \theta^k (1 - \theta)^{n-k} = \text{Bernoulli}(k | n, \theta)$

**CASE 2: Dataset being the count of heads**:

$\mathbb{P}(D | \theta) = {n \choose k} \theta^k (1 - \theta)^{n-k} = \text{Binomial}(k | n, \theta)$

---

**Sufficient statistics of the data and the equivalence of the above likelihoods**:

The sufficient statistics for a data assumed to be drawn by a probability distribution (our generative model) are the set of statistics of the data needed to infer the parameters of the probability distribution. More formally, $s(D)$ is the set of sufficient statistics for data $D$ if $\mathbb{P}(\theta | D) = \mathbb{P}(\theta | s(D))$. Consequently, given the same assumed probability distribution, if two datasets have the same sufficient statistics, we will infer the same value for the parameters of the probability distribution. In the case of the beta-binomial model as well as the beta-Bernoulli model, the sufficient statistics are $n$ and $k$.

We observe that the sufficient statistics are the exact same as the dataset of the count alone (where the order of heads and tails is not specified). In other words, whether we use the binomial model or the Bernoulli model, we get the same value for $\theta$. In other words, the posterior probability of observing $\theta$ given the observed data is the same whether we use the binomial model or the Bernoulli model

## Defining prior
KEY INTUITION 1: If we know something about the potential values of the mode parameter(s), we specify a certain distribution of potential parameter values.

---

**NOTE**: The distribution of potential parameter values would have certain parameters itself; these are called "hyperparameters", i.e. parameters for the distribution of the model parameter(s).

---

KEY INTUITION 2: If we know nothing about the potential values of the mode parameter(s), we assume an "uninformative prior".

---

The beta distribution is a versatile distribution that is easy to define and work with analytically while also being able to take a variety of distribution shapes. Furthermore, if the prior is distributed by a beta distirbution, it would the conjugate prior to a likelihood defined by a binomial or Bernoulli distribution, which means that in such a case, the posterior would also be distributed by a beta distribution. Hence, to define the distribution of potential values of our binomial generative model's parameter $\theta$, we consider a beta prior distribution:

$\text{Beta}(\theta | a, b) \propto \theta^{a-1}(1 - \theta)^{1-b}$

_To be more precise_...

$\text{Beta}(\theta | a, b) = \frac{\theta^{a-1}(1 - \theta)^{1-b}}{B(a, b)}$

Here, $B$ represents the beta function and $a$ and $b$ are the hyperparameters. The hyperparameters encode our prior beliefs about the potential values of $\theta$. If we know nothing about the potential values of $\theta$, then we take a uniform prior, which can be represented by a beta distribution with $a = b = 1$.
 
## Defining posterior
Mathematically, posterior  $\mathbb{P}(h|D)$ is the normalised value (i.e. value scaled to 0-1) of $\mathbb{P}(D|h) \mathbb{P}(h)$. Hence (assuming the dataset to be a particular sequence of IID binaries, i.e. it is an IID Bernoulli dataset):

$\mathbb{P}(h|D)$

$= \frac{\mathbb{P}(D|h) \mathbb{P}(h)}{\mathbb{P}(D)}$

$= \frac{1}{\mathbb{P}(D)} \theta^k (1 - \theta)^{n-k} \frac{\theta^{a-1}(1 - \theta)^{1-b}}{B(a, b)}$

$= \frac{1}{\mathbb{P}(D)} \frac{\theta^{k + a-1}(1 - \theta)^{n-k + 1-b}}{B(a, b)}$

---

The (unconditional) probability $\mathbb{P}(D)$ of the dataset D can be obtained through marginalisation:

$\mathbb{P}(D)$

$\displaystyle= \int_0^1 \mathbb{P}(\theta, D) d \theta$

$\displaystyle= \int_0^1 \mathbb{P}(D | \theta) \mathbb{P}(\theta) d \theta$

$\displaystyle= \int_0^1 \frac{\theta^{k + a-1}(1 - \theta)^{n-k + 1-b}}{B(a, b)} d \theta$

$\displaystyle= \int_0^1 \frac{B(k + a, n-k + b)}{B(a, b)} d \theta$ (based on the definition of the beta function)

---

Hence, we get the posterior as:

$\mathbb{P}(h|D)$

$= \frac{1}{\mathbb{P}(D)} \frac{\theta^{k + a-1}(1 - \theta)^{n-k + 1-b}}{B(k + a, n-k + b)}$

$= \text{Beta}(\theta | k + a, n-k + b)$

Hence, note that the prior and posterior densities are given by the same family of distributions under (possibly) distinct hyperparameters. For this reason, the beta PDF is said to be a conjugate prior for the likelihood function of an IID Bernoulli dataset.

# Maximum a posteriori (MAP) estimate of best hypothesis


# Posterior predictive distribution (PPD)

# Overfitting
