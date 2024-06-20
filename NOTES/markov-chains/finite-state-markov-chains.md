**FINITE STATE MARKOV CHAINS**

---

**Contents**:

- [Introduction](#introduction)
- [Transition probabilities](#transition-probabilities)
    - [1-step transition probabilities](#1-step-transition-probabilities)
    - [n-step transition probabilities](#n-step-transition-probabilities)

---

**MAIN REFERENCE**: ["Lecture 24: Finite-State Markov Chains" from _Part III: Random Processes_ from **Introduction to Probability**](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/pages/part-iii-random-processes/)

---

**NOTE**: In every topic, we shall assume time to be defined in discrete time steps, since it is easier to understand.

# Introduction
**NOTATION**:

- $X_n$ = The random variable denoting the state of the system at time stamp $n$
- $X_0$ = The random variable denoting the initial state of the system (can be given or random)

"Finite state" $\implies$ $X_n$ is one of a finite set of possible states

# Transition probabilities
## 1-step transition probabilities
**_More simply called "transition probabilities_**

Let $p_{ij}$ be the probability of the current state transitioning to state $j$ given the current state is $i$. Due to the Markov assumption, transition probabilities are time-homogenous, i.e. the only relevant information for the probability is the current state, not the time stamp.  In other words, the transition to the next state is predicted solely by the current state. Hence, more formally:

$p_{ij}$

$= \mathbb{P}(X_{n+1} = j | X_n = i)$

$= \mathbb{P}(X_1 = j | X_0 = i)$

**NOTE**: $\displaystyle \sum_{j=1}^{m} p_{ij} = 1$, where $i$ is fixed and ${1, 2 ... m}$ represents the exhaustive set of possible states.

## n-step transition probabilities
Let $r_{ij}(n)$ be the probability of the current state transitioning to state $j$ in $n$ time steps given the current state is $i$. Due to the Markov assumption, n-step transition probabilities are time-homogenous, i.e. the only relevant information for the probability is the current state and the number of time steps therefrom, not the time stamps themselves.  In other words, the transition to the next state after $n$ time steps is predicted solely by the current state and $n$. Hence, more formally:

$r_{ij}(n)$

$= \mathbb{P}(X_{s+n} = j | X_s = i)$

$= \mathbb{P}(X_n = j | X_0 = i)$

---

**NOTES**:

1.<br>

$\displaystyle \sum_{j=1}^{m} r_{ij}(n) = 1$, where $i$ and $n$ are fixed and ${1, 2 ... m}$ represents the exhaustive set of possible states.

2.<br>

$r_{ij}(0)$ means no transition takes place; it acts as an indicator for the current state, i.e. $r_{ij}(0) = 1$ if $i = j$ and $r_{ij}(0) = 0$ otherwise.

3.<br>

$r_{ij}(1) = p_{ij}$ (where $p_{ij}$ is the transition probability as defined in the last section).

---

**Recursive calculation of n-step transition probabilities**:

Note that $r_{ij}(n)$ is the same as the probability of transitioning to state $j$ in the step after step $n-1$, which means it is the total probability of transitioning from the current state $i$ to one of the possible states after n-1 steps and then transitioning to state $j$. Hence, given that ${1, 2 ... m}$ represents the exhaustive set of possible states:

$\displaystyle r_{ij}(n) = \sum_{k=1}^{m} r_{ik}(n-1) p_{kj}$ (where $p_{kj}$ is the (1-step) transition probability from state $k$ to state $j$)

Alternatively, note that $r_{ij}(n)$ is the same as the probability of transitioning to state $j$ in $n-1$ steps after first step, which means it is the total probability of transitioning from the current state $i$ to one of the possible states in the first step and then transitioning to state $j$ after $n-1$ steps. Hence, given that ${1, 2 ... m}$ represents the exhaustive set of possible states:

$\displaystyle r_{ij}(n) = \sum_{k=1}^{m} p_{ik} r_{kj}(n-1)$ (where $p_{ik}$ is the (1-step) transition probability from state $i$ to state $k$)

Both of the above are logically equivalent recursive formulas to calculate the n-step transition probability from state $i$ to state $j$.
