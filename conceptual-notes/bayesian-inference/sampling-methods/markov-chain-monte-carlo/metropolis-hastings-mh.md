**METROPOLIS-HASTINGS (MH)**

---

**Contents**:

- [Motivation](#motivation)
  - [Notation](#notation)
- [Defining the transition probability](#defining-the-transition-probability)
- [Defining the acceptance probability](#defining-the-acceptance-probability)
- [Metropolis algorithm](#metropolis-algorithm)

---

**Abbreviations**:

- MH: Metropolis-Hastings
- MCMC: Markov chain Monte Carlo

---

# Motivation
**_Why is it important?_**

MH is not a very modern or particularly efficient algorithm, but it is simple to understand and also provides a foundation to understand more sophisticated and powerful methods for sampling from and estimating the posterior distribution (paraphrased from ["1.2. A DIY Sampler, Do Not Try This at Home" from "1. Bayesian Inference" from _Bayesian Modeling and Computation in Python_](https://bayesiancomputationbook.com/markdown/chp_01.html)).

**NOTE**: _MH represents a class of methods, rather than a single method._

## Notation
- Let $f$ represent some function proportional to the target distribution $p$
- Let $g$ be the candidate distribution using which we shall take new samples

**NOTE**: _Commonly,_ $f$ _is the known numerator of_ $p$, _as in the case of_ $p$ _being the posterior in the context of Bayesian inference._

# Defining the transition probability
The transition probability is made of two components...

**1. Sampling probability**:

The next sample is sampled based on the current sample using an easier distribution $g$ whose parameters depend on the current sample. For example, we can define the probability of sampling $b$ given the current sample $a$ based on the distribution defined as $g(b | a) = \text{Normal}(a, \sigma^2)$.

**2. Acceptance probability**:

The next sample drawn based on the current sample is accepted or rejected based on the acceptance probability $A$. This is essentially the transition probability from the current state $a$ to the next state $b$ given that $b$ is what has been sampled after $a$ according to the sampling probability $g(b|a)$. It is denoted by $A(a \rightarrow b)$, read as "the probability of accepting the move from the sample $a$ to the proposed sample $b$".

---

Hence, the transition probability of going from state $a$ (i.e. sampling $a$) to state $b$ (i.e. sampling $b$) is the probability of sampling $b$ after $a$ and then accepting $b$. Mathematically, it is given by: $g(b|a) A(a \rightarrow b)$

# Defining the acceptance probability
How should the acceptance probability a.k.a. the transition probability $A$ be defined? Here, we use the detailed balance condition seen in MCMC (see: ["Detailed balance condition" from "Markov chain Monte Carlo"](#detailed-balance-condition)). Let $T(u|v)$ be the transition probability from state $v$ to state $u$, and let $\Theta$ be the sample space. Then, by the detailed balance condition:

$p(a) T(b|a) = p(b) T(a|b) \text{ } \forall a \in \Theta,  \text{ } \forall b \in \Theta$

We know that $f$ is proportional to $p$. Let $p(x) = \frac{f(x)}{N}$, for some $N$. Then:

$\frac{f(x)}{N} g(b|a) A(a \rightarrow b) = \frac{f(x)}{N} g(a|b) A(b \rightarrow a)$

$\implies \frac{A(a \rightarrow b)}{A(b \rightarrow a)} = \frac{f(a)}{f(b)} \frac{g(a|b)}{g(b|a)}$

---

For convenience, put $\frac{f(a)}{f(b)} = r_f$ and $\frac{g(a|b)}{g(b|a)} = r_g$. Then:

$\frac{A(a \rightarrow b)}{A(b \rightarrow a)} = r_f r_g$

Now, given that we know $A$ defines a probability, we know that $A(a \rightarrow b) \leq 1$ and $A(b \rightarrow a) \leq 1$.

---

Using the above inequalities and equation, we get the following cases:

1. $r_f r_g < 1 \implies A(a \rightarrow b) = r_f r_g$ and $A(b \rightarrow a) = 1$
2. $r_f r_g \geq 1 \implies A(a \rightarrow b) = 1$ and $A(b \rightarrow a) = \frac{1}{r_f r_g}$

We can simplify the above cases as follows:

$A(a \rightarrow b) = \max(1, r_f r_g)$

---

**INTUITION FOR THE ABOVE**:

For simplicity, let us assume $g$ is symmetrical, i.e. $g(a|b) = g(b|a)$. Hence:

$\frac{A(a \rightarrow b)}{A(b \rightarrow a)} = \frac{f(b)}{f(a)} \frac{g(a|b)}{g(b|a)} = \frac{f(a)}{f(b)}$

Hence, we have that:

$A(a \rightarrow b) = \max(1, r_f r_g) = \max(1, r_f) = \max(1, \frac{f(b)}{f(a)})$

Now, note that $p(x) = \frac{f(x)}{N}$, for some $N$. Hence:

$A(a \rightarrow b) = \max(1, \frac{f(b)}{f(a)}) = \max(1, \frac{p(b)}{p(a)})$

Hence, we have the following cases:

1. $p(b) > p(a) \implies A(a \rightarrow b) = 1$
2. $p(b) < p(a) \implies A(a \rightarrow b) = \frac{p(b)}{p(a)}$

What does this mean, practically? It means that if $b$ is a sample from a higher-probability-mass region of the target distribution $p$ than $a$, then it will certainly be accepted, which makes sense because we want to sample more from higher-probability-mass regions. However, if $b$ is a sample from a lower-density region of the target distribution $p$ than $a$, then it may or may not be accepted from $a$. Furthermore, we see that the probability of accepting $b$ from $a$ is lesser the lesser the density of $b$ is compared to the density of $a$, which also makes sense because we want there to be a lower but non-zero chance of sampling from a sparser region after sampling from a denser region, with the condition that the lower the density, the lower the chance. We see how such a policy is an MCMC method that helps estimate the target distribution more accurately and more efficiently over time.

# Metropolis algorithm
- The Metropolis algorithm is a special case of MH
- In Metropolis, the candidate distribution $g$ is strictly symmetrical
- On the other hand, MH can have an asymmetrical candidate distribution as well