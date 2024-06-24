**PREDICTIVE DISTRIBUTIONS**

---

**Contents**:

- [Prior predictive distribution (PrPD)](#prior-predictive-distribution-prpd)
- [Posterior predictive distribution (PPD)](#posterior-predictive-distribution-ppd)

---

**Main resource** https://bayesiancomputationbook.com/markdown/chp_01.html

---

The posterior distribution is the central object in Bayesian statistics, but it is not the only one. Besides making inferences about parameter values, we may want to make inferences about potential data, more precisely, the expections about the data before we observe it (such data may be either the current data or the future data). Predictive distributions are tools to make such inferences.

---

**Notation**:

- $D$ = Observed data so far
- $D^*$ = Expected or potential data
- $\mathbb{P}$ = Probability measure
- $\theta$ = A specific model <br> ..._often represented by a specific set of parameter values_
- $\Theta$ = The exhaustive set of models being considered <br> ..._usually of a specific generalised definition, e.g. a specific family of distributions_

# Prior predictive distribution (PrPD)
The PrPD is the distribution of expected data $D^*$ according to the generalised model $\Theta$ (whose expectations are quantified by the prior and likelihood), without having observed any data. In other words, it is the data we expect, given the generalised model, before actually observing any data. Hence, the PrPD tells us about the nature of the generalised model in and of itself. Mathematically, the PrPD is given by:

$\displaystyle \mathbb{P}(D^*) = \int_{\theta \in \Theta} \mathbb{P}(D^* | \theta) \mathbb{P}(\theta) d \theta$

**NOTE**: $\mathbb{P}(D^*) = \mathbb{P}(D^* | \Theta)$, since $\mathbb{P}(D^*)$ is essentially the marginal probability of getting the potential data $D^*$ with the model kept variable, i.e. with the model having been generalised.

The expression for the PrPD looks similar to the denominator component of Bayesian inference. However, unlike the denominator, PrPD is based on a likelihood (i.e. $\mathbb{P}(D^* | \theta)$) that is not conditioned by any observed data.

---

**Relevance of PrPD**:

We can use samples from the PrPD as a way to evaluate and calibrate our models using domain-knowledge. For example, we may ask questions such as "Is it okay for a model of human heights to predict that a human is negative 1.5 meters tall?". Even before measuring a single person, we can recognize the absurdness of the question. Hence, in general, the PrPD can help inform the validity or lack thereof in one's modeling choices.

# Posterior predictive distribution (PPD)

- $D$ = Observed data so far
- $D^*$ = Expected or potential data
- $\mathbb{P}$ = Probability measure
- $\theta$ = A specific model <br> ..._often represented by a specific set of parameter values_
- $\Theta$ = The exhaustive set of models being considered <br> ..._usually of a specific generalised definition, e.g. a specific family of distributions_

**NOTE**: $\Theta$ has a specific definition such that it generalises over the various specific models we want to consider. Hence, it can be considered a generalised model in its own right, wherein certain parameters are variable; each set of specific parameter values represents a specific instance or subclass of the generalised model.

The PPD is the distribution of expected (i.e. future) data $D^*$ according to the posterior $\mathbb{P}(\theta | D)$ for every $\theta \in \Theta$, which in turn is a consequence of the generalised model $\Theta$ (whose expectations are quantified by the prior and likelihood) and the observed data $D$. In more common terms, this is the data the generalised model $\Theta$ is expecting to see after seeing the dataset $D$, i.e. these are the generalised model’s predictions based on the data observed so far. Mathematically, the PPD is given by:

$\displaystyle \mathbb{P}(D^* | D) = \int_{\theta \in \Theta} \mathbb{P}(D^* | \theta) \mathbb{P}(\theta | D) d \theta$

here, we can see that predictions of the generalised model are computed by integrating out (or marginalizing) over the posterior distribution of specific models, i.e. specific parameter values. As a consequence predictions computed this way will incorporate the uncertainty about our estimates.