**MARKOV CHAINS**

---

**Contents**:

- [Introduction](#introduction)
- [Markov property or assumption](#markov-property-or-assumption)
- [Further reading](#further-reading)

---

**MAIN REFERENCE**: ["Lecture 24: Finite-State Markov Chains" from _Part III: Random Processes_ from _Introduction to Probability_](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/pages/part-iii-random-processes/)

---

**NOTE**: In every topic, we shall assume time to be defined in discrete time steps, since it is easier to understand.

# Introduction

Before seeing the definition, consider the fact that a Markov chain (also called a Markov process) summarises the influence of the past on the future using the notion of a state, wherein the state evolves over time according to some probability distribution. Implicit in a Markov chain is the Markov property/assumption, which states that the current state has all the information needed to predict the next state.

```

Past ----> Future
    \     /
     State

```

In other terms, $state(t+1) = f(state(t), noise)$, where $f$ is a function.

---

_Now for the full definition_...

A Markov process or chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. Informally, this may be thought of as, "What happens next depends only on the state of affairs now." ([_Markov chain_, Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)

> FURTHER REFERENCES:
> - https://en.wikipedia.org/wiki/Markov_chain
> - https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/10%3A_Markov_Chains/10.01%3A_Introduction_to_Markov_Chains

# Markov property or assumption

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

# Further reading

- [Finite-State Markov Chains](https://github.com/pranigopu/mastersProject/blob/main/NOTES/markov-chains/finite-state-markov-chains.md)
- [Steady-State Behaviour of Markov Chains]()
