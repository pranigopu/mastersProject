**BETA-BINOMIAL MODEL**

---

**Contents**:

- [Key definitions](#key-definitions)
- [Introduction](#introduction)
- [Components of Bayesian inference w.r.t. beta-binomial model](#components-of-bayesian-inference-wrt-beta-binomial-model)
  - [Defining likelihood](#defining-likelihood)
  - [Defining prior](#defining-prior)
  - [Defining posterior](#defining-posterior)
- [Maximum a posteriori (MAP) estimate of best hypothesis](#maximum-a-posteriori-map-estimate-of-best-hypothesis)
- [Posterior predictive distribution (PPD)](#posterior-predictive-distribution-ppd)
- [Overfitting](#overfitting)
  - ["Zero frequency problem" or "Sparse data problem"](#zero-frequency-problem-or-sparse-data-problem)

---

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

$\mathbb{P}(D | \theta) = {n \count k} \theta^k (1 - \theta)^{n-k} = \text{Binomial}(k | n, \theta)$

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

To generalise our solution and define the distribution of potential values of our beta-binomial generative model's parameter $\theta$, we consider a beta prior distritbuion:

$\text{Beta}(\theta | a, b) \propto \theta^{a-1}(1 - \theta)^{1-b}$

Here, $a$ and $b$ are the hyperparameters.
 
## Defining posterior
Mathematically, posterior  $p(h|D)$ is the normalised value (i.e. value scaled to 0-1) of $p(D|h) p(h)$. Hence:

$p(h|D) \propto p(D|h) p(h)$

If $H$ is the exhaustive set of all hypotheses, then the posterior is given as:

$p(h|D) = \frac{p(D|h) p(h)}{\sum_{h' \in H} p(D|h')}$

Note that $\sum_{h' \in H} p(D, h')$ is the sum of the combined probabilities for every hypothesis with respect to the data. $p(D, h')$ is the probability of observing both the data $D$ and the hypothesis $h'$ together (not any one _given_ the other). In fact $p(D, h') = p(D|h') p(h')$. Hence, $\sum_{h' \in H} p(D, h') = \sum_{h' \in H} p(D|h') p(h')$; this makes it a suitable normalising value for $p(D|h) p(h)$.

_More on posterior_...

# Maximum a posteriori (MAP) estimate of best hypothesis

$\displaystyle \hat{h}^{MAP} = \text{arg} \max_h p(D|h) p(h) = \text{arg} \max_h (\log p(D|h) + \log p(h))$

Note that the likelihood $p(D|h)$ depends exponentially on $N$, i.e. the number of samples drawn, i.e. the size of the dataset $D$, whereas the prior term $p(h)$ stays constant. Hence, when we have enough data, the data overwhelms the prior. In fact, the MAP estimate converges to the maximum likelihood estimate (MLE) as $N \rightarrow \infty$.

**NOTE**: The MLE estimate, for reference, is: <br> $\displaystyle \hat{h}^{MLE} = \text{arg} \max_h p(D|h) = \text{arg} \max_h \log p(D|h)$

---

Hence, as $N \rightarrow \infty$, $\hat{h}^{MAP} \rightarrow \hat{h}^{MLE}$

---

Given these facts, if the true hypothesis is in the hypothesis space, then (since it has the lowest $\frac{1}{|h|}$ value) both the MAP and the MLE estimates will converge upon this hypothesis; hence, Bayesian inference is based on consistent estimators. Note that if the hypothesis space does not include the true hypothesis (which is usually the case), we will converge upon the closest hypothesis to the true hypothesis ("closeness" can be formalised, as shall be discussed later).

# Posterior predictive distribution (PPD)
In essence, PPD gives the probability of a certain observation belonging to a certain concept, given (1) the data and (2) the posteriors for each hypothesis. Hence, PPD is basically the formalisation of a classifier based on the empirical evidence so far. In this way, it represents our "belief state" about the "world" (i.e. the environment we are dealing with). Mathematically, we have that:

$\displaystyle p(\tilde{x} \in C | D) = \sum_{h \in H} p(\tilde{x} \in C | h) p(h|D)$

Here:

- $D$: Dataset
- $C$: Concept by which we classify observations
- $H$: Hypothesis space, i.e. the set of all hypotheses to be considered
- $\tilde{x}$: Some observation

We can see that PPD is the weighted average of the probability of each hypothesis being the true hypothesis given the data. The weighting for each hypothesis is done using the probability of the observation $\tilde{x}$ belonging to the concept $C$ given that the hypothesis is true.

Note that each hypothesis $h$ represents an assumption about the sample space from which $\tilde{x}$ is drawn, and remember that each hypothesis is essentially a concept whose extension is proposed to be the sample space from which the data is drawn. $C$, on the other hand, is more specific concept that may be a subset of one or more of the hypotheses. Hence, PPD gives the posterior probability for an observation belonging to a specific concept (which may be either one of our hypotheses or a subset of one or more of our hypotheses) given the posterior probabilities for each of our hypotheses being true.

# Overfitting
## "Zero frequency problem" or "Sparse data problem"
The MLE of PPD can perform poorly if the sample size is small (since unrepresentative samples are more likely the smaller the samples are). Zero frequency problem is when estimation of frequency (of some variable's occurrence in general, beyond what has been observed) is zero due to zero observed instances.

_Why is this a problem?_

Because this problem makes us assign certainty (absolute impossibility, in this case) to enumeration-based induction. Enumeration cannot lead to certainty in induction, only probabilities; hence, it is misleading to assign certainty to something (a prediction or an estimation) that is not certain.

_Why is this problem relevant?_

_How to solve this problem?_
