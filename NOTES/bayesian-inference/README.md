**BAYESIAN INFERENCE**

---

**Contents**:

- [Bayesian modelling as a kind of conceptual modelling](#bayesian-modelling-as-a-kind-of-conceptual-modelling)
- [Components of Bayesian inference](#components-of-bayesian-inference)
  - [Posterior distribution (our target)](#posterior-distribution-our-target)
  - [Likelihood](#likelihood)
  - [Prior](#prior)
  - [Denominator](#denominator)
  - [Estimation of the components](#estimation-of-the-components)
    - [Estimating the denominator](#estimating-the-denominator)
    - [Estimating the posterior](#estimating-the-posterior)
- [Bayesian vs. frequentist](#bayesian-vs-frequentist)

---

"_Even if expressing statistical methods is easier than ever, statistics is a field full of subtleties that do not magically disappear by using powerful computation methods._" (quote from: ["1. Bayesian Inference" from _Bayesian Computation Book_](https://bayesiancomputationbook.com/markdown/chp_01.html)).

# Bayesian modelling as a kind of conceptual modelling
A conceptual model is a sufficiently abstract and useful representation of an entity or a system. Here, "abstract" means only relevant details are considered and irrelevant deatils are omitted. Note that "relevance" and "sufficiency" is w.r.t. the given context and purpose. Hence, a conceptual model is a useful essentialisation of an entity or a system.

Bayesian modelling is the process of inferring a conceptual model that explains the observed data. Here, the conceptual model is a generative model, i.e. a model that generates data based on a well-defined random process. Bayesian modelling consists of (1) proposing a conceptual model, (2) making assumptions about the model before any observations are taken into account, (3) taking observations into account, and (4) measuring the plausibility of the model given the prior assumptions and the observed data. Hence, we see that Bayesian modelling has the following needs:

- Domain expertise (for deciding the models and making prior assumptions)
- Statistical skill (for taking the observed data into account)

---

_Hence, Bayesian modelling integrates statistics with domain expertise to make a useful application of statistics._

---

In Bayesian modelling, the conceptual model may be defined in many ways, such as: a well-defined sample space, a theoretical distribution, etc. In practice, more than one conceptual model are considered and evaluated, since the choice of model is not always certain and having more models lets us compare potential models before making our choice. For example, if we consider the conceptual model to be a certain distribution from a family of distributions, i.e. if the conceptual model is a certain kind of statistical distribution (e.g. normal, binomial, etc.) with certain parameter values, then Bayesian inference is done to figure out the plausibility of any given choice of parameter values. As another example, if we consider the conceptual model to be a certain sample space from a set of possible sample spaces, then Bayesian inference is done to figure out the plausibility of getting the observed data from any given choice of sample space. Hence, we see that Bayesian modelling also has the following more specific needs:

- Data (the raw material)
- Statistical distributions (the mathematical tools to shape the models)

---

**NOTE 1**: Hence, note that a theoretical distribution with the parameters kept variable, such as the normal distribution with unknown mean and variance, represent not one conceptual model but a range of possible conceptual models corresponding to the possible values of the mean and variance. In some texts, the theoretical distribution as a whole may be considered as a conceptual model, but I reject such a definition since it makes Bayesian modelling harder to explain and generalise for cases where conceptual models are not theoretical distributions.

**NOTE 2**: The terms "model" and "process" can also refer to observations from a population of entities, wherein the model or process is based on the distribution of a certain charateristic in the population.

**NOTE 3**: In practice, when dealing with a family of theoretical distributions as the basis for conceptual models, we represent the chosen models with a set of parameter values, given the family of distributions being considered.

# Components of Bayesian inference
- $\theta$: Chosen model
- $D$: Observed data

## Posterior distribution (our target)
The probability of our chosen model being the true model given the observed data. Hence, it is:

$P(\theta | D)$

## Likelihood
The probability of our chosen model generating the observed data. More precisely, it is the probability of our chosen model generating data that is the same as the observed data. Hence, it is:

$P(D | \theta)$

## Prior
The probability of the true model being the same as our chosen model (note that the "true model" refers to the actual process generating the observed data). Hence, it is:

$P(\theta)$

---

**RELATIONSHIP BETWEEN POSTERIOR, LIKELIHOOD AND PRIOR**:

The posterior $P(\theta | D)$ is the normalised value of $P(D | \theta) P(\theta)$. Hence:

$P(\theta | D) \propto P(D | \theta) P(\theta)$

## Denominator
The total probability of getting the observed data across all the potential models. Hence, we see that the denominator is the appropriate normalisation constant for $P(D | \theta) P(\theta)$. Note that given a set of potential models, the denominator is constant. The denominator is given by:

_For a discrete hypothesis space of models_...

$\displaystyle P(D) = \sum_{\theta' \in \Theta} P(D | \theta') P(\theta')$

_For a continuous hypothesis space of models_...

$\displaystyle P(D) = \int_{\theta' \in \Theta} P(D | \theta') P(\theta')$

_Hence, we also see that the denominator is the marginal probability of getting the observed data with the model kept variable._

## Estimation of the components
### Estimating the denominator
- Jeffrey's rule
- Reference

### Estimating the posterior
- Analytical
    - _Possible of likelihood and prior are conjugates (discussed later)_
- Computational

# Bayesian vs. frequentist
**Bayesian**:

Focuses on the uncertainty of underlying conditions that generate certain outcomes. Hence, the potential underlying models are distributed probabilistically. In other words, the Bayesian approach measures the quality of the evidence (i.e. the observed data) for a hypothesis (i.e. a hypothesised model).

**Frequentist**:

Focuses on the uncertainty of the outcomes given certain underlying conditions. Hence, the potential outcomes are distributed probabilistically. In other words, the frequentist approach measures the expected proportional frequency of potential outcomes based on past outcomes.