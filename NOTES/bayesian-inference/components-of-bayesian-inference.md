**COMPONENTS OF BAYESIAN INFERENCE**

---

**Contents**:

- [Posterior distribution (our target)](#posterior-distribution-our-target)
- [Likelihood](#likelihood)
- [Prior](#prior)
- [Denominator](#denominator)
- [Estimation of the components](#estimation-of-the-components)
  - [Estimating the denominator](#estimating-the-denominator)
  - [Estimating the posterior](#estimating-the-posterior)

---

**Notation**:

- $\theta$: Chosen model
- $D$: Observed data
- $p$ = Probability mass function (for discrete domains) or probability density function (for continuous domains)

# Posterior distribution (our target)
The probability of our chosen model being the true model given the observed data. Hence, it is:

$p(\theta | D)$

# Likelihood
The probability of our chosen model generating the observed data. More precisely, it is the probability of our chosen model generating data that is the same as the observed data. Hence, it is:

$p(D | \theta)$

# Prior
The probability of the true model being the same as our chosen model (note that the "true model" refers to the actual process generating the observed data). Hence, it is:

$p(\theta)$

---

**RELATIONSHIP BETWEEN POSTERIOR, LIKELIHOOD AND PRIOR**:

The posterior $p(\theta | D)$ is the normalised value of $p(D | \theta) p(\theta)$. Hence:

$p(\theta | D) \propto p(D | \theta) p(\theta)$

---

# Denominator
The total probability of getting the observed data across all the potential models. Hence, we see that the denominator is the appropriate normalisation constant for $p(D | \theta) p(\theta)$. Note that given a set of potential models, the denominator is constant. The denominator is given by:

_For a discrete hypothesis space of models_ $\Theta$...

$\displaystyle p(D) = \sum_{\theta' \in \Theta} p(D | \theta') p(\theta')$

_For a continuous hypothesis space of models_ $\Theta$...

$\displaystyle p(D) = \int_{\theta' \in \Theta} p(D | \theta') p(\theta')$

Hence, we also see that the denominator is the marginal probability of getting the observed data with the model kept variable, i.e. with the model having been generalised. Therefore, it is valid to say that $p(D) = p(D | \Theta)$, where $\Theta$ is the generalised model, i.e. the class of models that generalises all the specific models being considered.

# Estimation of the components
## Estimating the denominator
- Jeffrey's rule
- Reference

## Estimating the posterior
- Analytical
    - _Possible of likelihood and prior are conjugates (discussed later)_
- Computational
