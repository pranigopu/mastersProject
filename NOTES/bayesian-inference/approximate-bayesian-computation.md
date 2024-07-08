**APPROXIMATE BAYESIAN COMPUTATION (ABC)**

---

**Contents**:

- [Introduction](#introduction)
- [Basic formulation](#basic-formulation)
  - [Using distance between datasets](#using-distance-between-datasets)
  - [Using distance between summary statistics](#using-distance-between-summary-statistics)
- [Basic approach](#basic-approach)
  - [ABC-rejection sampler](#abc-rejection-sampler)
  - [Use of sequential Monte Carlo (SMC)](#use-of-sequential-monte-carlo-smc)
- [Choosing ABC hyperparameters](#choosing-abc-hyperparameters)
  - [Choosing the distance function](#choosing-the-distance-function)
  - [Choosing tolerance values](#choosing-tolerance-values)
  - [Choosing summary statistics](#choosing-summary-statistics)

---

# Introduction
"Approximate" in ABC refers to the lack of explicit likelihood; it does not refer to the use of numerical methods to approximate the posterior (which need an explicit likelihood), such as Markov chain Monte Carlo (MCMC) or Variational Inference (VI). Hence, another (common and more explicit) name for ABC methods is likelihood-free methods (note that some authors differentiate between these terms while others use them interchangeably).

ABC methods may be useful when we do not have an explicit expression for the likelihood, but have a parameterised (i.e. parameter-based) simulator capable of generating synthetic data. The simulator has one or more unknown parameters, and our goal with ABC methods is to know which set of parameters generates synthetic data close enough to the observed data. To achieve our goal, we shall compute a posterior distribution for the simulator's parameters.

---

**NOTE 1**: ABC is especially relevant if not only there is no closed-form solution for the likelihood but it is also unfeasible to estimate the likelihood computationally using the simulator.

**NOTE 2**: From the perspective of the ABC method, the simulator is a black-box where we feed parameter values at one side and get simulated data from the other.

---

Difficulties with ABC:

- Defining what "close enough" means in the absence of a likelihood
- Being able to actually compute an approximated posterior for the parameters

# Basic formulation
## Using distance between datasets
**Notation**:

- $\theta$: Simulator parameter(s)
- $Sim$: Simulator instantiator
- $D$: Observed data
- $\tilde{D}$: Synthetic (simulated) data
- $P$ = Probability measure

We have that:

$\tilde{D} \sim Sim(\theta)$

Now, we define the distance function $\delta$ such that:

$\displaystyle \lim_{\epsilon \rightarrow 0} \delta(D, \tilde{D} | \epsilon) = P(D|\theta)$

Here:

- $P(D|\theta)$ is the likelihood for the observed data $D$
- $\epsilon$ is the tolerance parameter (i.e. numerically defines "close enough")
- $\delta(D, \tilde{D} | \epsilon)$ is the distance between $D$ and $\tilde{D}$ given $\epsilon$ tolerance

**NOTE**: _We introduce a tolerance parameter_ $\epsilon$ _because the chance of generating a synthetic dataset being equal to the observed data is virtually zero for most problems. The larger the value of_ $\epsilon$ _the more tolerant we are about how close $D$ and $\tilde{D}$ has to be in order to consider them as close enough. In general and for a given problem, a larger the tolerance parameter value implies a more crude approximation to the posterior._

---

Hence, we get the posterior as follows:

$P(\theta|D) \sim \propto \delta(D, \tilde{D} | \epsilon) P(\theta)$

---

**NOTE 1**: $P(\theta)$ is the prior.

**NOTE 2**: $\sim \propto$ means "approximately proportional to".

## Using distance between summary statistics
In practice, as we increase the sample size or dimensionality of the data, it becomes increasingly harder to generate simulated data close enough to the observed data, which means it becomes increasingly harder to find small enough values for the distance function. A naive solution is to increase the value of the tolerance $\epsilon$, but this means increasing the error of our approximation.

A more effective solution could be to instead use one or more summary statistics and compute the distance between these summary statistics of each dataset instead of computing the distance between the simulated and real datasets. To formalise this idea: let $S(Y)$ be the the tuple of summary statistics for any dataset $Y$. Then, instead of $\delta(D, \tilde{D} | \epsilon)$, we use $\delta(S(D), S(\tilde{D}) | \epsilon)$.

Note that using a summary statistic introduces an additional source of error to the ABC approximation, unless the summary statistics are sufficient with respect to the simulator's parameter(s). However, it is not always possible to find sufficient statistics for the simulator's parameter(s). Even so, the summary statistics can be useful. (_How? Not sure yet._)

**NOTE**: _If using more than one summary statistic, each with a different distance computation and possibly with a different scale,_ $\epsilon$ _would be a list of thresholds corresponding to the list of distance computations for each summary statistic._

---

**NOTE: Sufficient statistics**:

The sufficient statistics for a model's parameter (the model being the simulator in our case) are the set of statistics of the model-generated data such that the statistics are sufficient to infer the parameters of the model. More formally, $S(D)$ is the set of sufficient statistics for data $D$ if $P(\theta|D) = P(\theta|S(D))$. For example, for data drawn from a normal distribution, the sample mean is the sufficient statistic for the distribution mean.

# Basic approach
## ABC-rejection sampler
The most basic method to perform ABC is rejection sampling:

- Sample a value of $\theta$ from the prior distribution
- Pass that value to the simulator and generate synthetic data $\tilde{D}$
- If $\tilde{D}$ is at a distance $\delta < \epsilon$, save the proposed $\theta$, else reject it
- Repeat until having the desired number of samples

**NOTE**: _The above method approximates the posterior distribution._

## Use of sequential Monte Carlo (SMC)
If the prior distribution is too different from the posterior distribution, then the ABC-rejection sampler will spend most of the time proposing values that will be rejected. A more effective (and efficient) approach is to propose from a prior distribution closer to the actual posterior. Generally, we do not know enough about the posterior to do this by hand, but we can achieve it using a sequential Monte Carlo (SMC) method (which is a general sampler method under which fall many specific methods).

**NOTE**: _SMC adapted to perform ABC is called SMC-ABC._

# Choosing ABC hyperparameters
## Choosing the distance function
There are many ways to compute the distancce between two datasets or two sets of summary statistics. The appropriate distance function is the one that most suits the specific domain or problem. The L2 norm (Euclidean distance), the L1 norm (sum of absolute differences, also called the Laplace distance), the $\text{L}\infty$ norm (maximum of the absolute differences) and the Mahalanobis distance are popular options.

_Distances for datasets vs. distances for summary statistics_...

Distances such as Gaussian, Laplace, etc. can be applied either to datasets or to summary statistics. However, there are also some distance functions that are meant to provide good results without the use of summary statistics. Two such distances are: Wasserstein distances and the Kullback-Leibler (KL) divergence. Such distances may be desirable due to the difficulty in many cases in choosing appropriate summary statistics.

---

**Why sort the datasets before calculating distances?**

Samples are drawn independently, which means drawing a smaller value has no effect on the probability of drawing a larger value and vice versa. Hence, two samples with the same values may be ordered differently. Hence, the order of the sample's values has no effect on its information about the model, simulator or distribution it was drawn from. Now, when calculating the distance between two different samples with the same values, depending on the ordering of each sample, we may get different distances. For example, if by chance the samples were ordered such that one sample is the reverse of the other, the distance would be very large, whereas if the samples were ordered in the same way, the distance would be zero. Hence, we see that if we sort first, we can see that the samples are the same.

**KEY POINT**:  _The above applies only under the assumption that the sample values are drawn independently. If not, sorting can destroy the structure in the data; an example would be a time series, where sample values are not independent to each other._

## Choosing tolerance values
**Options available**:

In many ABC methods the value of the tolerance $\epsilon$ works as a hard threshold, such that $\theta$ values generating samples with distance larger than $\epsilon$ are rejected. Alternatively, $\epsilon$ can be a list of decreasing values that the user has to set or the algorithm finds adaptively.

---

**General guidelines to choose** $\epsilon$:

To find a useful value of $\epsilon$, we may take these educated guesses as upper bound, after which we try also a few lower values. We could then choose a final value of $\epsilon$ based on several factors, including the computational cost, the needed level of precision/error and the efficiency of the sampler.

---

**High** $\epsilon$ **values vs. low** $\epsilon$ **values**:

Note that the lower the $\epsilon$ value, the greater the accuracy of the approximation. However, if $\epsilon$ is too low, we would be aiming for an unfeasible or unnecessary level of accuracy, making the sampler inefficient, wherein the approximation fails to converge over time.

---

**Tolerance for multiple summary statistics**:

If we instead use more than one summary statistics, then we can set $\epsilon$ to a list of values. This is usually necessary as each summary statistic may have a different scale. If the scales are too different then the contribution of each summary statistic will be uneven, it may even occur that a single summary statistic dominates the computed distances. Some popular choices for $\epsilon$ for a summary statistic are empirical standard deviation of the given statistic and median absolute deviation of the given statistic.

## Choosing summary statistics
A suitable set of summary statistics provides a balance between low dimensionality and informativeness. When we do not have a sufficient summary statistic, it is tempting to overcompensate by adding a lot of summary statistics under the intuition that more information is preferable. There are two problems with such an approach. (1) We move from computing distances over datasets to distances over summary statistics to reduce the dimensionality; hence, by increasing the number of summaries statistics we are defeating that purpose. (2) Increasing the number of summary statistics can reduce the quality of the approximated posterior due to the higher dimensionalilty of the set of summary statistics used; such a reduction in quality can happen due to (a) more inappropriate summary statistics mixed with appropriate ones, (b) higher distance values due to higher dimensionality of the set of summary statistics used.