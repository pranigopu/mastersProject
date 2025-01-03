**QUANTIFYING PRIOR INFORMATION**

---

**Contents**:

- [Conjugate priors](#conjugate-priors)
- [Objective priors](#objective-priors)
  - [Jeffrey's prior](#jeffreys-prior)
- [Maximum entropy priors](#maximum-entropy-priors)
  - [PRELIMINARY CONCEPT: Entropy](#preliminary-concept-entropy)
  - [MAIN CONCEPT: The principle of maximum entropy](#main-concept-the-principle-of-maximum-entropy)
- [Weakly informative priors a.k.a. regularisation priors](#weakly-informative-priors-aka-regularisation-priors)
- [Using prior predictive distributions to decide on priors](#using-prior-predictive-distributions-to-decide-on-priors)

---

> **Main resource**: ["1. Bayesian Inference" from _Bayesian Computation Book_](https://bayesiancomputationbook.com/markdown/chp_01.html)

---

"_Even if expressing statistical methods is easier than ever, statistics is a field full of subtleties that do not magically disappear by using powerful computation methods._" (quote from: ["1. Bayesian Inference" from _Bayesian Computation Book_](https://bayesiancomputationbook.com/markdown/chp_01.html)).

# Conjugate priors
Consider a Bayesian model wherein the likelihood and the prior are defined using theoretical distributions. If the prior is defined with respect to the likelihood such that the posterior's theoretical distribution is of the same kind (i.e. the same family of distributions) as the prior, then we say that the chosen prior is a conjugate prior to the likelihood.

For example in a beta-binomial distribution (see: [_Beta-binomial model_ from **Generative models for discrete data**](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/generative-models-for-discrete-data/beta-binomial-model.md)), we see that if the likelihood is defined using a binomial distribution, then choosing a beta-distributed prior results in a beta-distributed posterior. Here, a beta distribution is a conjugate prior to the binomial-distributed likelihood.

---

Conjugate priors enable us to obtain the posterior distribution analytically, which can save computational load, since we do not have to estimate the posterior distribution using sampling. Furthermore, having an analytically describable posterior distribution can help improve the accuracy of the Bayesian inference (provided the likelihood and prior are well-founded). Lastly, having an analytically describable posterior distribution can make the Bayesian model more interpretable.

# Objective priors
In the absence of prior information, one may follow the principle of indifference, also known as the principle of insufficient reason, which essentially says that lack of informationa about a problem means there is no reason to consider any outcome to be more likely than any other. In the context of Bayesian statistics, this principle has motivated the study and use of **objective priors**, _which are systematic ways of generating priors that have the least possible influence on the modelling process for the given problem_. If there is insufficient information, objective priors eliminate the subjectivity from prior elicitation.

---

**NOTE 1**: There are other sources of subjectivity apart from prior elicitation, such as the choice of the likelihood, the data selection process, the choice of the problem being modelled or investigated, etc.

**NOTE 2**: There is no way to make a prior totally uninformative; the inclusion of a prior necessarily includes at least some information and/or assumptions about the problem or the model. Even if we assume that all outcomes are equally likely, it is still an assumption. It is not a fault but a feature; Bayesian modelling presupposes at least some information and/or assumptions, and is not meant to operate from a state of total ignorance.

## Jeffrey's prior
A kind of uninformative prior that does not presuppose any particular kind of model definition. In other words, for any model definition used, the posterior obtained using a Jeffrey's prior — i.e. a Jeffrey's posterior — can be transformed to the Jeffrey's posterior for any other model definition. In other words, a Jeffrey's prior makes no assumption about the way a model is parameterised; it is invariant under reparametrisation.

**NOTE**: _How the Jeffrey's posterior for one model can be transformed into the Jeffrey's posterior for another model? That is beyond the scope of my notes here. For more information,_ see: [An introduction to Jeffreys priors - 1](https://www.youtube.com/watch?v=S42N_6pQ5TA).

# Maximum entropy priors
## PRELIMINARY CONCEPT: Entropy
The entropy of a system is the measure of uncertainty we have about the outcomes of the system. Hence, note that entropy is defined with respect to our knowledge and is thus an epistemological concept here, rather than a physical or metaphysical concept. Hence, note that whenever we talk about the entropy of a system, we are always talking about it with respect to our knowledge about the system. Also note that when we talk about the entropy of a distribution, we are talking about the entropy of a system whose outcomes follow the given distribution.

The more we know about how likely one outcome is compared to the others, the less uncertainty we have about the outcomes of the system and thus the less entropy the system has. Conversely, the less we know about how likely one outcome is compared to the others, the more uncertainty we have about the outcomes of the system and thus the more entropy the system has. Hence, entropy measures our uncertainty about the distribution of the outcomes of the system.

**NOTE**: _A system is any complex integration of entities and their interactions, e.g. a complex entity, a model, a population, a process, etc. A system, hence, is a generic term for anything that behaves a certain way so as to produce certain outcomes._

## MAIN CONCEPT: The principle of maximum entropy
Given our prior knowledge/assumptions about a system, the principle of maximum entropy states that the probability distribution which best represents our uncertainty about a system (i.e. about its potential outcomes) is the one with largest entropy. Note that prior knowledge/assumptions about a system also represent prior knowledge/assumptions about the probability distribution of its outcomes.

More precisely, the principle of maximum entropy states the following: (1) Take the precisely stated prior data and/or testable information about a probability distribution function. (2) Consider the set of all conceivable probability distributions that would encode the prior data. (3) Then, according to this principle, the distribution with maximal information entropy is the best choice.

**NOTE**: _Given no prior knowledge/assumptions about a system, the uniform distribution of outcomes the distribution with the maximal information entropy._

---

**Some examples of applying the principle of maximum entropy**:

The distributions with the largest entropy under the following constraints are:

| Contraints | Maximal entropy distribution |
| --- | --- |
| none | uniform |
| +ve mean, support $[0, \infty)$ | exponential |
| given absolute deviation to mean, support $(-\infty, \infty)$ | Laplace |
| given mean and variance, support $(-\infty, \infty)$ | normal |
| only two unordered outcomes, constant mean | binomial |

---

**NOTE 1**: For the last case, we use Poisson if we have rare events; Poisson can be seen as a special case of binomial.

**NOTE 2**: Laplace distribution is also called the double exponential distribution.

---

> For further references for and/or validation of the principle:
>
> - [Principle of maximum entropy (Wikipedia)](https://en.wikipedia.org/wiki/Principle_of_maximum_entropy)
> - ["The Principle of Maximum Entropy" by Mutual Information (YouTube)](https://www.youtube.com/watch?v=2gTrsLVnp9c)

# Weakly informative priors a.k.a. regularisation priors
For many problems, we often have information about the possible values a parameter of our model for the problem. Such information can be derived in many ways, e.g. the possible range based on the physical meaning of the parameter, the plausible range based on previous experiments/observations, etc.. For example, we know heights must be positive. We can use such information to weakly inform our analysis, i.e. to keep our model within reasonable bounds without making strong assumptions. Priors based on such information are called weakly informative priors; what makes a prior a weakly informative prior is based more on empirical or model-driven factors than on a well-defined mathematical framework.

Regularisation is a procedure of adding information with the aim of solving an ill-posed problem or to reduce the chance of overfitting and priors offer a principled way of performing regularisation. Hence, because weakly-informative priors work to keep the posterior distribution within reasonable bounds, they are also known as regularising priors.

---

**Regularisation priors to prevent overfitting**:

Overfitting occurs when a model makes predictions very close to the dataset used to fit it, but it fails to fit additional data and/or predict future observations with reasonable accuracy. In other words, overfitting occurs when a model is fine-tuned to specifics that may be uncommon in general. Hence, overfitting is the failure to generalise the model. A regularisation prior can help correct for overfitting by ensuring that the model is aligned with at least some reasonable expectations about the system or process being modelled. Hence, Bayesian modelling generalises the process of regularisation, since any regularisation parameter such as, say a cost function of a machine learning algorithm, can be understood as a regularisation prior of a Bayesian model.

**NOTE**: _The counterpart of overfitting is underfitting, which is when a model fails to adequately capture the underlying structure of the data._

# Using prior predictive distributions to decide on priors
**For notes on prior predictive distributions, see**: ["Prior predictive distribution (PrPD)" from _Predictive Distributions_](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/predictive-distributions.md#prior-predictive-distribution-prpd)

The prior predictive distribution (PrPD) of a generalised model is the distribution of the data that could be expected, given the prior (i.e. the encoded prior knowledge and/or assumptions) we have chosen. Using the distribution, we can see what prior or range of priors would lead to a reasonable and/or plausible expectation of potential data. In other words, using the PrPD allows us to get reasonable/plausible priors based on our knowledge what is reasonable and/or plausible to expect about the thing (a system or a population) that we want to model.

Additionally, computing the prior predictive distribution to some extent could help us ensure our model has been properly written and is able to run in our probabilistic programming language; it can even help us to debug our model. Later, we shall see more concrete examples of how to reason about prior predictive samples and use them to choose reasonable priors. In practice, we can compute a prior predictive distribution by sampling from the model, but without conditioning on the observed data. By sampling from the prior predictive distribution, the computer does the work of translating choices we made in the parameter space into the observed data space. Using these samples to evaluate priors is known as prior predictive checks (referenced from: ["Understanding Your Assumptions" from _2. Exploratory Analysis of Bayesian Models_ from **Bayesian Computation Book**](https://bayesiancomputationbook.com/markdown/chp_02.html#understanding-your-assumptions)).
