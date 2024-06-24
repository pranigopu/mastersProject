**BAYESIAN INFERENCE**

---

**Contents**:

- [Bayesian modelling as a kind of conceptual modelling](#bayesian-modelling-as-a-kind-of-conceptual-modelling)
- [Bayesian vs. frequentist](#bayesian-vs-frequentist)
- [Further reading](#further-reading)

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

# Bayesian vs. frequentist
**Bayesian**:

Focuses on the uncertainty of underlying conditions that generate certain outcomes. Hence, the potential underlying models are distributed probabilistically. In other words, the Bayesian approach measures the quality of the evidence (i.e. the observed data) for a hypothesis (i.e. a hypothesised model).

**Frequentist**:

Focuses on the uncertainty of the outcomes given certain underlying conditions. Hence, the potential outcomes are distributed probabilistically. In other words, the frequentist approach measures the expected proportional frequency of potential outcomes based on past outcomes.

# Further reading
1. [Components of Bayesian Inference]()