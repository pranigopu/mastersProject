**APPROXIMATE BAYESIAN COMPUTATION (ABC)**

---

**Contents**:

- [Introduction](#introduction)
- [Basic formulation](#basic-formulation)
  - [Using distance between datasets](#using-distance-between-datasets)
  - [Using distance between summary statistics](#using-distance-between-summary-statistics)

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
- $\tilde{D}$: Synthetic data
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
In practice, as we increase the sample size or dimensionality of the data, it becomes increasingly harder to generate simulated data close enough to the observed data, which means it becomes increasingly harder to find small enough values for the distance function. A naive solution is to increase the value of the tolerance $\epsilon$, but this means increasing the error of our approximation. A more effective solution could be to instead use one or more summary statistics and compute the distance between these summary statistics of each dataset instead of computing the distance between the simulated and real datasets.

Let $S(Y)$ be the the tuple of summary statistics for a dataset $Y$.

Hence, instead of $\delta(D, \tilde{D} | \epsilon)$, we use $\delta(S(D), S(\tilde{D}) | \epsilon)$.