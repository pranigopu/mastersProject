# NOTES

# Generative models for discrete data

## Key definitions

- **Concept**: Set of all units that fit a definition
- **Hypothesis**: A concept proposed to explain given data
- **Hypothesis space**: Set of all hypotheses being considered to explain given data
- **Likelohood**: Probability of observing certain data given a certain hypothesis is true
- **Prior**: Probability of a certain hypothesis being true prior to any observations
- **Posterior**: Probability of a certain hypothesis being true having observed certain data

KEY IDEA: Generalise discrete class using only positive examples

_Hence, emulate induction using probability calculus._

KEY CONCEPT: Posterior predictive distribution

## Defining likelihood
KEY INTUITION: Avoid suspicious coincidences

KEY ASSUMPTION: Assume examples are sampled uniformly at random from an extension of a concept

_This is the strong sampling assumption (Tenenbaum)._

Extension of a concept refers to the set of all referents of a concept. Hence, extension of the concept "all even numbers between 1-100" is {0, 2, ... 100}. Given the strong sampling assumption, the probability of sampling $N$ items with replacement from hypothesis class $h$ is given by:

$p(D|h) = [\frac{1}{size(h)}]^N = [\frac{1}{|h|}]^N$ ($D$ is the given data)

This equation is based on the size principle (Tenenbaum), i.e. the model favours the simplest hypothesis (i.e. one with the smallest extension) consistent with the data $D$ ("Occam's razor"). In essence, we consider the simplest hypothesis consistent with the data to be the most likely hypothesis; on this basis, likelihood $p(D|h)$ is defined.

**NOTE**: A hypothesis is, in essence, a concept assumed to explain the given data $D$. Hence, formally, a hypothesis is the same as a concept.

## Defining prior
KEY INTUITION: Conceptually "unnatural" or "contrived" hypotheses are less likely (prior to any observation)

_For example, "powers of 2 except 32" is less conceptually natural to "powers of 2", even if the former has higher "likelihood" as defined previously._

Defining priors can be controversial due to the ill-defined idea of "natural".

**NOTE**: Prior of hypothesis $h$ is written as $p(h)$.

## Defining posterior
Mathematically, posterior is the normalised value (i.e. value scaled to 0-1) of $p(h|D) = p(D|h) p(h)$.

If $H$ is the exhaustive set of all hypotheses, then the posterior is given as:

$p(h|D) = \frac{p(D|h) p(h)}{\sum_{h' \in H} p(D|h')}$

Note that $\sum_{h' \in H} p(D, h')$ is the sum of the combined probabilities for every hypothesis with respect to the data. $p(D, h')$ is the probability of observing both the data $D$ and the hypothesis $h'$ together (not any one _given_ the other). In fact $p(D, h') = p(D|h') p(h')$. Hence, $\sum_{h' \in H} p(D, h') = \sum_{h' \in H} p(D|h') p(h')$; this makes it a suitable normalising value for $p(D|h) p(h)$.

_More on posterior_...

### Maximum a posteriori (MAP) estimate of best hypothesis

$\displaystyle \hat{h}^{MAP} = \text{arg} \max_h p(D|h) p(h) = \text{arg} \max_h (\log p(D|h) + \log p(h))$

Note that the likelihood $p(D|h)$ depends exponentially on $N$, i.e. the number of samples drawn, i.e. the size of the dataset $D$, whereas the prior term $p(h)$ stays constant. Hence, when we have enough data, the data overwhelms the prior. In fact, the MAP estimate converges to the maximum likelihood estimate (MLE) as $N \rightarrow \infty$:

**NOTE**: The MLE estimate, for reference, is: <br> $\displaystyle \hat{h}^{MLE} = \text{arg} \max_h p(D|h) = \text{arg} \max_h \log p(D|h)$

---

Hence, as $N \rightarrow \infty$, $\hat{h}^{MAP} \rightarrow \hat{h}^{MLE}$

---

Given these facts, if the true hypothesis is in the hypothesis space, then (since it has the lowest $\frac{1}{|h|}$ value) both the MAP and the MLE estimates will converge upon this hypothesis; hence, Bayesian inference is based on consistent estimators. Note that if the hypothesis space does not include the true hypothesis (which is usually the case), we will converge upon the closest hypothesis to the true hypothesis ("closeness" can be formalised, as shall be discussed later).

### Posterior predictive distribution (PPD)
In essence, PPD gives the probability of a certain observation belonging to a certain concept, given (1) the data and (2) the posteriors for each hypothesis. Hence, PPD is basically the formalisation of a classifier based on the empirical evidence so far. In this way, it represents our "belief state" about the "world" (i.e. the environment we are dealing with). Mathematically, we have that:

$\displaystyle p(\tilde{x} \in C | D) = \sum_h p(y = 1 | \tilde{x}, h) p(h|D)$

Here:

- $D$: Dataset
- $C$: Concept by which we classify observations
- $\tilde{x}$: Some observation
- $y$: Output indicating whether or not $\tilde{x} \in C$ (1 if yes, 0 if no)

Note that each hypothesis $h$ represents an assumption about the sample space from which $\tilde{x}$ is drawn, and remember that each hypothesis is - in essence - a concept whose extension is proposed to be the sample space. $C$, however, is more specific concept that may be a subset of one of the hypotheses.
