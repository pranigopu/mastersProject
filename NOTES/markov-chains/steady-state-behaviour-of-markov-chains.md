**STEADY STATE BEHAVIOUR OF MARKOV CHAINS**

---

**Contents**:

- [Background](#background)
- [Sufficient conditions for steady-state behaviour](#sufficient-conditions-for-steady-state-behaviour)
- [Calculating steady-state probabilities](#calculating-steady-state-probabilities)

---

# Background
DRIVING QUESTION:

Does the probability of transitioning from any state to any state converge to some constant, given enough steps?

_More formally_...

Does $r_{ij}(n) = \mathbb{P}(X_n = j | X_0 = i$ converge to some $\pi_j$ for all $i$ and $j$?

---

**Reference for transition probability notation**: [_Finite State Markov Chains_](https://github.com/pranigopu/mastersProject/blob/main/NOTES/markov-chains/finite-state-markov-chains.md)

---

Key to answering the above question is to answer whether the initial state $i$ is relevant to the above probability. If yes, then the answer to the above question is no. Hence, we have the question: under what conditions is the initial state $i$ relevant in n-step transition probabilities as n tends to infinity? Here, consider the following cases:

---

_First, some definitions_...

- **Recurrent state**: A state is recurrent if, starting from it, there is always a way to return to it eventually
- **Transient state**: A state is transient if it is not recurrent, i.e. if, starting from it, there is not always a way to return to it
- **Recurrent class**: A group of recurrent states that can transition only between each other
- **Periodic states**: States in a recurrent class are periodic if all transitions lead from one distinct subclass to another distinct subclass <br> **NOTE**: _There may be more than 1 distinct subclasses, but there must be more than 1._

---

_Back to the cases_...

1.<br>

**If a Markov chain has more than 1 recurrent class**, then based on which recurrent class you start from, there is no probability of ever transitioning to a state in another recurrent class. Hence, the initial state here is relevant to at least some n-step transition probabilities as n tends to infinity.

2.<br>

**If a Markov chain has periodic states**, then given that you start from one of these states, the probability of transitioning to another periodic state evidently depends on the a cyclical progression and thus never converges. Hence, the initial state here is relevant to at least some n-step transition probabilities as n tends to infinity.

---

Hence, we know that the probability of transitioning from any state to any state does not converge for at least some states if either (1) the Markov chain has more than 1 recurrent class, or (2) the Markov chain has periodic states. However, while we know when the answer to the driving question is "no", when is it "yes"? We shall now see...

# Sufficient conditions for steady-state behaviour
THEOREM:

$r_{ij}(n) = \mathbb{P}(X_n = j | X_0 = i)$ converges to some $\pi_j$ for all $i$ and $j$ if:

1. Recurrent states are all in a single class, i.e. the Markov chain has only 1 recurrent class
2. The single recurrent class is not periodic, i.e. the Markov chain has no periodic states

**NOTE**: _The above are not necessary conditions, but they are sufficient conditions._

---

Hence, we know that the n-step transition probability of a Markov chain converges for any state as n approaches infinity provided that (1) the transition probabilities converge, and (2) the converging transition probabilities are independent of the initial state. Note again that these are only sufficient conditions, not necessary conditions. Hence, a Markov chain may converge even if one of these conditions are false.

# Calculating steady-state probabilities
ASSUMPTION: The Markov chain displays steady-state behaviour.

By the Markov property, we have that:

$\displaystyle r_{ij}(n) = \sum_{k=1}^m r_{ik}(n-1) p_{kj}$

As $n \rightarrow \infty$, given the Markov chain's steady-state behaviour:

$r_{ij}(n) = \pi_j$ and $\displaystyle \sum_{k=1}^m r_{ik}(n-1) p_{kj} = \sum_{k=1}^m \pi_{k} p_{kj}$

$\displaystyle \therefore \pi_j = \sum_{k=1}^m \pi_{k} p_{kj}$

Note that we have the above equation for all conceivable states $j \in {1, 2 ... m}$, and for each equation, the right-hand side gives us $m$ variables, namely $\pi_1, \pi_2 ... \pi_m$. Hence, when we consider all conceivable end states of the n-step transition, we get a system of $m$ linear equations with $m$ variables each. Note that "all conceivable end states" takes all the states into account, since we are considering the steady-state probabilities of all states.


Now, note that by itself, the system is singular, since $\pi_j = 0 \text{ } \forall j$ is a valid solution of the system. But when we consider the fact that each $\pi_j$ is a probability, and when we consider the fact that $\pi_1, \pi_2 ... \pi_m$ are the steady-state probabilities of the exhaustive set of possible states ${1, 2 ... m}$, we have that:

$\displaystyle \sum_{j=1}^m \pi_j= 1$

Adding this equation to system, we see that $\pi_j = 0 \text{ } \forall j$ is an invalid solution, making the system non-singular, which means we can get exact steady-state probabilities by soliving the system.
