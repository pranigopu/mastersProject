**GENERATIVE MODELS FOR DISCRETE DATA**

---

**Contents**:

- [Introduction](#introduction)
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

# Bayesian concept learning
In Bayesian concept learning, the generative models are represented using a "concept", i.e. a set of all units that fit a definition. Note that the concept represents the sample space from which data can be drawn. Hence, we try to find the most plausible concept, i.e. the most plausible sample space from which the observed data could have been drawn. In other words, we try to learn the most plausible concept which the observed data may fall under.

[Read more >>](https://github.com/pranigopu/mastersProject/blob/main/NOTES/generative-models-for-discrete-data/bayesian-concept-learning.md)

# Beta-binomial model
In beta-binomial models, the generative models are represented by the parameters of a binomial distribution and a beta distribution; the binomial distribution is for the likelihood component of Bayesian inference, whereas the beta distribution is for the prior component of Bayesian inference. It is a useful model because a prior defined by a beta distribution is a conjugate prior to a likelihood defined by a binomial distribution, which means the posterior distribution can be obtained analytically (rather than computationally) as a beta distribution as well. Furthermore, the beta-binomial model is the basis of naive Bayes classifiers and Markov models.

[Read more >>](https://github.com/pranigopu/mastersProject/blob/main/NOTES/generative-models-for-discrete-data/beta-binomial-model.md)

# Dirichlet-multinomial model

# Naive Bayes classifiers
