<h1>NOTES</h1>

**_A Conceptual Introduction to Hamiltonian Monte Carlo_**

---

**Contents**:

- [The issue with estimating expectations using probability density](#the-issue-with-estimating-expectations-using-probability-density)
  - [Why is this issue important to explore?](#why-is-this-issue-important-to-explore)
  - [Introducing the issue](#introducing-the-issue)
  - [Explaining part of the issue using the geometry of high dimensional spaces](#explaining-part-of-the-issue-using-the-geometry-of-high-dimensional-spaces)
  - [Explaining part of the issue using the geometry of high dimensional distributions](#explaining-part-of-the-issue-using-the-geometry-of-high-dimensional-distributions)
  - [Explaining the value of MCMC and especially HMC](#explaining-the-value-of-mcmc-and-especially-hmc)

---

**NOTE**: _I will mostly be excerpting from the original paper._

---

**Abbreviations**:

- HMC: Hamiltonian Monte Carlo
- MCMC: Markov chain Monte Carlo

# The issue with estimating expectations using probability density
## Why is this issue important to explore?

It shows why sampling around modes is insufficient for estimating high-dimensional distributions. Hence, shows the necessity for more sophisticated methods of sampling from a distribution to estimate its key features (e.g. shape, spread, mean, etc.), especially in higher dimensional spaces. Hamiltonian Monte Carlo (HMC) is one such method, but before learning about it, we need to see why bother with such methods at all.

## Introducing the issue
In practice we often are interested in computing expectations with respect to many target functions, for example in Bayesian inference we typically summarize our uncertainty with both means and variances, or multiple quantiles. Any method that depends on the specific details of any one function will then have to be repeatedly adjusted for each new function we encounter, expanding a single computational problem into many. Consequently, from here on in we will assume that any relevant function is sufficiently uniform in parameter space that its variation does not strongly effect the integrand.

This assumption implies that the variation in the integrand is dominated by the target density, and hence we should consider the neighborhood around the mode where the density is maximized. This intuition is consistent with the many statistical methods that utilize the mode, such as maximum likelihood estimators and Laplace approximations, although conflicts with our desire to avoid the specific details of the target density. Indeed, this intuition is fatally naive as it misses a critical detail.

Expectation values are given by accumulating the integrand over a volume of parameter space and, while the density is largest around the mode, there is not much volume there. To identify the regions of parameter space that dominate expectations we need to consider the behavior of both the density and the volume. In high-dimensional spaces the volume behaves very differently from the density, resulting in a tension that concentrates the significant regions of parameter space away from either extreme

## Explaining part of the issue using the geometry of high dimensional spaces
_One of the characteristic properties of high-dimensional spaces is that there is much more volume outside any given neighborhood than inside of it._ For example, consider partitioning parameter space into rectangular boxes centered around the mode (see figure below). In one dimension there are only two partitions neighboring the center partition, leaving a significant volume around the mode. Adding one more dimension, however, introduces eight neighboring partitions, and in three dimensions there are already 26. In general there are 3D −1 neighboring partitions in a D-dimensional space, and for even small D the volume neighboring the mode dominates the volume immediately around the mode.

![Understanding the distribution of volume in high dimensional spaces; example 1](https://github.com/pranigopu/mastersProject/blob/main/reading/images/understanding-distribution-of-volume-in-high-dim-spaces-1.png)

(Source: [_A Conceptual Introduction to Hamiltonian Monte Carlo_ by Michael Betancourt](https://arxiv.org/pdf/1701.02434))

---

_Another example to illustrate the above point_...

Alternatively, we can take a spherical view of parameter space and consider the relative volume a distance δ inside and outside of a spherical shell (Figure 2). In one dimension the interior and exterior volumes are equal, but in two and three dimensions more and more volume concentrates on the outside of the shell. Centering the shell at the mode we can see once again that the volume in any neighborhood containing the mode becomes more and more negligible as the dimension of the parameter space increases.

![Understanding the distribution of volume in high dimensional spaces; example 2](https://github.com/pranigopu/mastersProject/blob/main/reading/images/understanding-distribution-of-volume-in-high-dim-spaces-2.png)

(Source: [_A Conceptual Introduction to Hamiltonian Monte Carlo_ by Michael Betancourt](https://arxiv.org/pdf/1701.02434))

---

Generically, then, volume is largest out in the tails of the target distribution away from the mode, and this disparity grows exponentially with the dimension of parameter space. Consequently, the massive volume over which we integrate can compensate to give a significant contribution to the target expectation despite the smaller density. In order to identify the neighborhoods that most contribute to expectations, we need to carefully balance the behavior of both the density and the volume.

## Explaining part of the issue using the geometry of high dimensional distributions
The neighborhood immediately around the mode features large densities, but in more than a few dimensions the small volume of that neighborhood prevents it from having much contribution to any expectation. On the other hand, the complimentary neighborhood far away from the mode features a much larger volume, but the vanishing densities lead to similarly negligible contributions expectations. The only significant contributions come from the neighborhood between these two extremes known as the typical set.

**NOTE**: _Hence, a typical set is the region of the target distribution is the region that gives the most information about the target distribution._

As the dimension of parameter space increases, the tension between the density and the volume grows and the regions where the density and volume are both large enough to yield a significant contribution becomes more and more narrow. Consequently the typical set becomes more singular with increasing dimension, a manifestation of concentration of measure. The immediate consequence of concentration of measure is that the only significant contributions to any expectation come from the typical set; evaluating the integrand outside of the typical set has negligible effect on expectations and hence is a waste of precious computational resources. In other words, we can accurately estimate expectations by averaging over the typical set instead of the entirety of parameter space. Consequently, in order to compute expectations efficiently, we have to be able to identify, and then focus our computational resources into, the typical set.

![Illustration of typical set](https://github.com/pranigopu/mastersProject/blob/main/reading/images/illustration-of-typical-set.png)

(Source: [_A Conceptual Introduction to Hamiltonian Monte Carlo_ by Michael Betancourt](https://arxiv.org/pdf/1701.02434))

## Explaining the value of MCMC and especially HMC
Of course, understanding why we want to focus on the typical set in only the first step. How to construct an algorithm that can quantify the typical set of an arbitrary target distribution is another problem altogether. There are many strategies for this task, but one of the most generic, and hence most useful in applied practice, is Markov chain Monte Carlo (MCMC).

Now, the simplest MCMC method is the Random Walk Metropolis method, whose generalisation is the Metropolis-Hastings method (see: [_Metropolis-Hastings (MH)_ from **Sampling Methods** from **Bayesian Inference** from `conceptual-notes`](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo/metropolis-hastings-mh.md)). However, the guess-and-check strategy of Random Walk Metropolis is doomed to fail in highdimensional spaces where there are an exponential number of directions in which to guess but only a singular number of directions that stay within the typical set and pass the check (i.e. the Metropolis acceptance criterion).

Hence, In order to make large jumps away from the initial point, and into new, unexplored regions of the typical set, we need to exploit information about the geometry of the typical set itself. Specifically, we need transitions that can follow those contours of high probability mass, coherently gliding through the typical set. Hamiltonian Monte Carlo (HMC) is the unique procedure for automatically generating this coherent exploration for sufficiently well-behaved target distributions (more precisely, HMC achieves the desired exploration by carefully exploiting the differential structure of the target probability density).

For an illustration, see below:

**Deficiency of Random Walk Metropolis sampling**:

![Random Walk Metropolis sampling](https://github.com/pranigopu/mastersProject/blob/main/reading/images/random-walk-metropolis-sampling.png)

**Efficiency of contour-based sampling (e.g. HMC)**:

![Contour-based sampling](https://github.com/pranigopu/mastersProject/blob/main/reading/images/contour-based-sampling.png)

- Red: High-probability-mass contour of the target distribution
- Green: Points sampled from the target distribution

(Source: [_A Conceptual Introduction to Hamiltonian Monte Carlo_ by Michael Betancourt](https://arxiv.org/pdf/1701.02434))

