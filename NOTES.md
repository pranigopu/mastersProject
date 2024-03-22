# NOTES

## Generative models for discrete data
KEY IDEA: Generalise discrete class using only positive examples

_Hence, emulate induction using probability calculus._

KEY CONCEPT: Posterior predictive distribution

### Defining likelihood
KEY INTUITION: Avoid suspicious coincidences

KEY ASSUMPTION: Assume examples are sampled uniformly at random from an extension of a concept

_This is the strong sampling assumption (Tenenbaum)._

Extension of a concept refers to the set of all referents of a concept. Hence, extension of the concept "all even numbers between 1-100" has the extension {0, 2, ... 100}. Given the strong sampling assumption, the probability of sampling $N$ items with replacement from hypothesis class $h$ is given by:

$p(D|h) = [\frac{1}{size(h)}]^N = [\frac{1}{|h|}]^N$ ($D$ is the given data)

This equation is based on the size principle (Tenenbaum), i.e. the model favours the simplest (smallest) hypothesis consistent with the data $D$ ("Occam's razor"). In essence, we consider the simplest hypothesis consistent with the data to be the most likely hypothesis; on this basis, likelihood $p(D|h)$ is defined.

### Defining prior
KEY INTUITION: Conceptually "unnatural" or "contrived" hypotheses are less likely (prior to any observation)

_For example, "powers of 2 except 32" is less conceptually natural to "powers of 2", even if the former has higher "likelihood" as defined previously._
