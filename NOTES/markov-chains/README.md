**MARKOV CHAINS**

---

**Contents**:

- [Introduction](#introduction)
- [Markov property/assumption](#markov-property-assumption)

---

# Introduction

A Markov process summarises the influence of the past on the future using the notion of a state, wherein the state evolves over time according to some probability distribution.

```

Past -----> Future
    \     /
     State

```

In other terms, $state(t+1) = f(state(t), noise)$, where $f$ is a function.

# Markov property/assumption

A key property/assumption implicit in a Markov process is that given the current state, the past does not matter. In other terms:

- All the information relevant to predict the future state is contained in the current state
- Adding more information about the past does not affect the transition probabilities <br> **NOTE**: _Transition probability_ $implies$ _The probability of the current state transitioning to one of the possible states_
- The probability distribution of the next state depends on the past only through the current state

More formally:

$p_{ij} = \mathbb{P}(X_{n+1} | X_n = i) = \mathbb{P}(X_{n+1} | X_n = i, X_{n-1} ... X_1, X_0)$

Here:

- $p_{ij}$ = The transition probability from state $i$ to state $j$ (1-step transition probability)
- $\mathbb{P}$ = Probability measure
- $X_k$ = The random variable denoting the state at the $k$-th time step

Hence, how the model is specified, i.e. how the states and state transitions are represented is crucial.

