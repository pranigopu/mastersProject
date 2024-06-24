**GENERATIVE MODELS FOR DISCRETE DATA**

---

**Contents**:

- [Introduction](#introduction)
- [Posterior predictive distribution (PPD)](#posterior-predictive-distribution-ppd)
- [Various discrete generative models and / or use-cases](#various-discrete-generative-models-and--or-use-cases)
  - [Bayesian concept learning](#bayesian-concept-learning)
  - [Beta-binomial model](#beta-binomial-model)
  - [Dirichlet-multinomial model](#dirichlet-multinomial-model)
  - [Naive Bayes classifiers](#naive-bayes-classifiers)

---

# Introduction
A generative model means a model that generates data based on a well-defined random process. For example, a Gaussian generative model generates data based on a normal distribution. In practice, a generative model is proposed to explain the observed data by showing how and with what likelihood the model could generate to the observed data. I  practice, we try to find the most plausible generative model that explains the observed data. As the topic name suggests, we shall explore generative models that draw data from discrete sample spaces rather than continuous sample spaces.

For each kind of generative model, we shall define:

- The likelihood
- The prior
- The posterior
- The posterior predictive distribution (PPD)

# Posterior predictive distribution (PPD)
> KEY REFERENCE: https://bayesiancomputationbook.com/markdown/chp_01.html

- $D$ = Observed data so far
- $D^*$ = Expected or potential data
- $\mathbb{P}$ = Probability measure
- $\theta$ = A specific model <br> ..._often represented by a specific set of parameter values_
- $\Theta$ = The exhaustive set of models being considered <br> ..._usually of a specific generalised definition, e.g. a specific family of distributions_

**NOTE**: If $\Theta$ has a specific definition (which is generally the case), then it can be considered a general model in its own right, wherein certain parameters are variable; each set of specific parameter values represents a specific instance or subclass of the general model.

_Likelihood, prior and posterior have been discussed in_ [**Bayesian Inference**](https://github.com/pranigopu/mastersProject/tree/main/NOTES/bayesian-inference). _Hence, I shall focus on the new concept, i.e. PPD._

PPD is the distribution of expected (i.e. future) data $D^*$ according to the posterior $\mathbb{P}(\theta | D)$ for every $\theta \in \Theta$, which in turn is a consequence of the general model $\Theta$ (whose expectations are quantified by the prior and likelihood) and the observed data $D$. In more common terms, this is the data the general model $\Theta$ is expecting to see after seeing the dataset $D$, i.e. these are the general model’s predictions based on the data observed so far. Mathematically, the PPD is given by:

$\mathbb{P}(D^* | D) = \int_{\theta \in \Theta} \mathbb{P}(D^* | \theta) \mathbb{P}(\theta | D) d \theta$

here, we can see that predictions of the general model are computed by integrating out (or marginalizing) over the posterior distribution of specific models, i.e. specific parameter values. As a consequence predictions computed this way will incorporate the uncertainty about our estimates.

# Various discrete generative models and / or use-cases
## Bayesian concept learning
In Bayesian concept learning, the generative models are represented using a "concept", i.e. a set of all units that fit a definition. Note that the concept represents the sample space from which data can be drawn. Hence, we try to find the most plausible concept, i.e. the most plausible sample space from which the observed data could have been drawn. In other words, we try to learn the most plausible concept which the observed data may fall under.

[Read more >>](https://github.com/pranigopu/mastersProject/blob/main/NOTES/generative-models-for-discrete-data/bayesian-concept-learning.md)

## Beta-binomial model
In beta-binomial models, the generative models are represented by the parameters of a binomial distribution and a beta distribution; the binomial distribution is for the likelihood component of Bayesian inference, whereas the beta distribution is for the prior component of Bayesian inference. It is a useful model because a prior defined by a beta distribution is a conjugate prior to a likelihood defined by a binomial distribution, which means the posterior distribution can be obtained analytically (rather than computationally) as a beta distribution as well. Furthermore, the beta-binomial model is the basis of naive Bayes classifiers and Markov models.

[Read more >>](https://github.com/pranigopu/mastersProject/blob/main/NOTES/generative-models-for-discrete-data/beta-binomial-model.md)

## Dirichlet-multinomial model

## Naive Bayes classifiers
