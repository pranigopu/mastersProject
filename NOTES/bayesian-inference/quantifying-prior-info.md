**QUANTIFYING PRIOR INFORMATION**

---

**Contents**:

- [Conjugate priors](#conjugate-priors)
- [Objective priors](#objective-priors)

---

# Conjugate priors
Consider a Bayesian model wherein the likelihood and the prior are defined using theoretical distributions. If the prior is defined with respect to the likelihood such that the posterior's theoretical distribution is of the same kind (i.e. the same family of distributions) as the prior, then we say that the chosen prior is a conjugate prior to the likelihood.

For example in a beta-binomial distribution (see: [_Beta-binomial model_ from **Generative models for discrete data**](https://github.com/pranigopu/mastersProject/blob/main/NOTES/generative-models-for-discrete-data/beta-binomial-model.md)), we see that if the likelihood is defined using a binomial distribution, then choosing a beta-distributed prior results in a beta-distributed posterior. Here, a beta distribution is a conjugate prior to the binomial-distributed likelihood.

---

Conjugate priors enable us to obtain the posterior distribution analytically, which can save computational load, since we do not have to estimate the posterior distribution using sampling. Furthermore, having an analytically describable posterior distribution can help improve the accuracy of the Bayesian inference (provided the likelihood and prior are well-founded). Lastly, having an analytically describable posterior distribution can make the Bayesian model more interpretable.

# Objective priors
In the absence of prior information, one may follow the principle of indifference, also known as the principle of insufficient reason, which essentially says that lack of informationa about a problem means there is no reason to consider any outcome to be more likely than any other. In the context of Bayesian statistics, this principle has motivated the study and use of **objective priors**, _which are systematic ways of generating priors that have the least possible influence on the modelling process for the given problem_. If there is insufficient information, objective priors eliminate the subjectivity from prior elicitation.

---

**NOTE 1**: There are other sources of subjectivity apart from prior elicitation, such as the choice of the likelihood, the data selection process, the choice of the problem being modelled or investigated, etc.

**NOTE 2**: There is no way to make a prior totally uninformative; the inclusion of a prior necessarily includes at least some information and/or assumptions about the problem or the model. Even if we assume that all outcomes are equally likely, it is still an assumption. It is not a fault but a feature; Bayesian modelling presupposes at least some information and/or assumptions, and is not meant to operate from a state of total ignorance.
