# NOTES

## Generative models for discrete data
KEY IDEA: Generalise discrete class using only positive examples

_Hence, emulate induction using probability calculus._

KEY CONCEPT: Posterior predictive distribution

### Defining likelihood
KEY INTUITION: Avoid suspicious coincidences

KEY ASSUMPTION: Assume examples are sampled uniformly at random from an extension of a concept

_This is the strong sampling assumption (Tenenbaum)._

Extension of a concept refers to the set of all referents of a concept. Hence, extension of the concept "all even numbers between 1-100" is {0, 2, ... 100}. Given the strong sampling assumption, the probability of sampling $N$ items with replacement from hypothesis class $h$ is given by:

$p(D|h) = [\frac{1}{size(h)}]^N = [\frac{1}{|h|}]^N$ ($D$ is the given data)

This equation is based on the size principle (Tenenbaum), i.e. the model favours the simplest hypothesis (i.e. one with the smallest extension) consistent with the data $D$ ("Occam's razor"). In essence, we consider the simplest hypothesis consistent with the data to be the most likely hypothesis; on this basis, likelihood $p(D|h)$ is defined.

**NOTE**: A hypothesis is, in essence, a concept assumed to explain the given data $D$. Hence, formally, a hypothesis is the same as a concept.

### Defining prior
KEY INTUITION: Conceptually "unnatural" or "contrived" hypotheses are less likely (prior to any observation)

_For example, "powers of 2 except 32" is less conceptually natural to "powers of 2", even if the former has higher "likelihood" as defined previously._

Defining priors can be controversial due to the ill-defined idea of "natural".

**NOTE**: Prior of hypothesis $h$ is written as $p(h)$.

### Defining posterior
Mathematically, posterior is the normalised value (i.e. value scaled to 0-1) of $p(h|D) = p(D|h) p(h)$.

If $H$ is the exhaustive set of all hypotheses, then the posterior is given as:

$p(h|D) = \frac{p(D|h) p(h)}{\sum_{h' \in H} p(D|h')}$

Note that $\sum_{h' \in H} p(D, h')$ is the sum of the combined probabilities for every hypothesis with respect to the data. $p(D, h')$ is the probability of observing both the data $D$ and the hypothesis $h'$ together (not any one _given_ the other). In fact $p(D, h') = p(D|h') p(h')$. Hence, $\sum_{h' \in H} p(D, h') = \sum_{h' \in H} p(D|h') p(h')$; this makes it a suitable normalising value for $p(D|h) p(h)$.

#### Maximum a posteriori (MAP) estimate of best hypothesis

$\displaystyle \hat{h}^{MAP} = \text{arg} \max_h p(D|h) p(h) = \text{arg} \max_h (\log p(D|h) + \log p(h))$

Note that the likelihood $p(D|h)$ depends exponentially on $N$, i.e. the number of samples drawn, i.e. the size of the dataset $D$, whereas the prior term $p(h)$ stays constant. Hence, when we have enough data, the data overwhelms the prior; the MAP estimate converges to the maximum likelihood estimate (MLE) $\displaystyle \text{arg} \max_h p(D|h) = \text{arg} \max_h \log p(D|h)$
