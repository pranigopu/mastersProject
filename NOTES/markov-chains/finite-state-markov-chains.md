**FINITE STATE MARKOV CHAINS**

---

**Contents**:



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

$p_{ij}$ is the probability of the current state transitioning to state $j$ given the current state is $i$. Due the Markov assumption, transition probabilities are time-homogenous, i.e. the only relevant information for the probability is the current state, not the time stamp.  In other words, the transition to the next state is predicted solely by the current state. Hence, more formally:

$p_{ij}$

$= \mathbb{P}(X_{n+1} = j | X_n = i)$

$= \mathbb{P}(X_1 = j | X_0 = i)$

**NOTE**: $\sum_{j=1}^{m} p_{ij} = 1$, where ${1, 2 ... m}$ represents the exhaustive set of possible states.
