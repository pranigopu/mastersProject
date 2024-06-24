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

# Posterior distribution (our target)
The probability of our chosen model being the true model given the observed data. Hence, it is:

$P(\theta | D)$

# Likelihood
The probability of our chosen model generating the observed data. More precisely, it is the probability of our chosen model generating data that is the same as the observed data. Hence, it is:

$P(D | \theta)$

# Prior
The probability of the true model being the same as our chosen model (note that the "true model" refers to the actual process generating the observed data). Hence, it is:

$P(\theta)$

---

**RELATIONSHIP BETWEEN POSTERIOR, LIKELIHOOD AND PRIOR**:

The posterior $P(\theta | D)$ is the normalised value of $P(D | \theta) P(\theta)$. Hence:

$P(\theta | D) \propto P(D | \theta) P(\theta)$

---

# Denominator
The total probability of getting the observed data across all the potential models. Hence, we see that the denominator is the appropriate normalisation constant for $P(D | \theta) P(\theta)$. Note that given a set of potential models, the denominator is constant. The denominator is given by:

_For a discrete hypothesis space of models_ $\Theta$...

$\displaystyle P(D) = \sum_{\theta' \in \Theta} P(D | \theta') P(\theta')$

_For a continuous hypothesis space of models_ $\Theta$...

$\displaystyle P(D) = \int_{\theta' \in \Theta} P(D | \theta') P(\theta')$

_Hence, we also see that the denominator is the marginal probability of getting the observed data with the model kept variable._

# Estimation of the components
## Estimating the denominator
- Jeffrey's rule
- Reference

## Estimating the posterior
- Analytical
    - _Possible of likelihood and prior are conjugates (discussed later)_
- Computational