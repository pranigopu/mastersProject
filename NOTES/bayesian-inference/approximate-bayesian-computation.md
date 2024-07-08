**APPROXIMATE BAYESIAN COMPUTATION (ABC)**

---

**Contents**:

- [Introduction](#introduction)
- [Basic formulation](#basic-formulation)

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
**Notation**:

- $\theta$: Simulator parameter(s)
- $Sim$: Simulator instantiator
- $D$: Observed data
- $D'$: Synthetic data
- $P$ = Probability measure

We have that:

$D' \sim Sim(\theta)$

Now, we define the distance function $\delta$ such that:

$\displaystyle \lim_{\epsilon \rightarrow 0} \delta(D, D' | \epsilon) = P(D|\theta)$

Here:

- $P(D|\theta)$ is the likelihood for the observed data $D$
- $\epsilon$ is the tolerance parameter (i.e. numerically defines "close enough")
- $\delta(D, D' | \epsilon)$ is the distance between $D$ and $D'$ given $\epsilon$ tolerance

**NOTE**: _We introduce a tolerance parameter_ $\epsilon$ _because the chance of generating a synthetic dataset being equal to the observed data is virtually zero for most problems. The larger the value of_ $\epsilon$ _the more tolerant we are about how close $D$ and $D'$ has to be in order to consider them as close enough. In general and for a given problem, a larger the tolerance parameter value implies a more crude approximation to the posterior._

---

Hence, we get the posterior as follows:

$P(\theta|D) \utilde{\propto} \delta(D, D' | \epsilon) P(\theta)$

**NOTE**: $P(\theta)$ _is the prior._
