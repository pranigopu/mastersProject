<h1>NOTES</h1>

**_A Conceptual Introduction to Hamiltonian Monte Carlo_**

---



---

# The issue with estimating expectations using probability density
## Why is this issue important to explore?

It shows why sampling around modes is insufficient for estimating high-dimensional distributions. Hence, shows the necessity for more sophisticated methods of sampling from a distribution to estimate its key features (e.g. shape, spread, mean, etc.), especially in higher dimensional spaces. Hamiltonian Monte Carlo (HMC) is one such method, but before learning about it, we need to see why bother with such methods at all.

## Introducing the issue
In practice we often are interested in computing expectations with respect to many target functions, for example in Bayesian inference we typically summarize our uncertainty with both means and variances, or multiple quantiles. Any method that depends on the specific details of any one function will then have to be repeatedly adjusted for each new function we encounter, expanding a single computational problem into many. Consequently, from here on in we will assume that any relevant function is sufficiently uniform in parameter space that its variation does not strongly effect the integrand.

This assumption implies that the variation in the integrand is dominated by the target density, and hence we should consider the neighborhood around the mode where the density is maximized. This intuition is consistent with the many statistical methods that utilize the mode, such as maximum likelihood estimators and Laplace approximations, although conflicts with our desire to avoid the specific details of the target density. Indeed, this intuition is fatally naive as it misses a critical detail.

Expectation values are given by accumulating the integrand over a volume of parameter space and, while the density is largest around the mode, there is not much volume there. To identify the regions of parameter space that dominate expectations we need to consider the behavior of both the density and the volume. In high-dimensional spaces the volume behaves very differently from the density, resulting in a tension that concentrates the significant regions of parameter space away from either extreme

## Explaining the issue using the geometry of higher dimensional spaces
_One of the characteristic properties of high-dimensional spaces is that there is much more volume outside any given neighborhood than inside of it._ For example, consider partitioning parameter space into rectangular boxes centered around the mode (see figure below). In one dimension there are only two partitions neighboring the center partition, leaving a significant volume around the mode. Adding one more dimension, however, introduces eight neighboring partitions, and in three dimensions there are already 26. In general there are 3D −1 neighboring partitions in a D-dimensional space, and for even small D the volume neighboring the mode dominates the volume immediately around the mode.

![Understanding the distribution of volume in high dimensional spaces](https://github.com/pranigopu/mastersProject/blob/main/reading/images/understanding-distribution-of-volume-in-high-dim-spaces.png)