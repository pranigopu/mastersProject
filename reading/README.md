# Master's project

## Key criteria for project topic
- Ensure that the topic produces valuable intermediate steps
    - The value addition must begin as early in the research as possible
    - It is risky to work on something that only works as a complex integration of many parts

### Possible topics
- Comparing Bayesian methods for neural networks
    - Stage 1: Empirical comparison (i.e. understanding what)
    - Stage 2: Understanding the empirical results theoretically (i.e. understanding why)
- Extending model-based reinforcement learning methods using Bayesian methods

## Project resources
- Benchmark for testing reinforcement learning models
    - https://michelangeloconserva.github.io/Colosseum/mds/intro.html
- Murphy, Kevin P. Machine Learning: A Probabilistic Perspective, 2012 (IMPORTANT)
    - Check chapters 3 and 7
- Paulo Rauber notes on the above (summarises first 17 chapters of the above) (IMPORTANT)
    - https://www.paulorauber.com/files/notes/machine_learning.pdf
    - Check chapters 3 and 7 (corresponds to chapters 3 and 7 of Murphy's book)
    - **NOTE**: Is less readable but more mathematically rigorous than Murphy's book
- Bayesian computation online textbook (IMPORTANT)
    - https://bayesiancomputationbook.com/markdown/chp_01.html
- Hands-on Bayesian Neural Networks - A Tutorial for Deep Learning Users
    - https://arxiv.org/pdf/2007.06823.pdf
- Posterior Sampling for Deep Reinforcement Learning (IMPORTANT)
    - https://arxiv.org/pdf/2305.00477.pdf

## POTENTIAL AREA: Bayesian computation (especially in neural networks)
### Advantages of Bayesian approach in machine learning
1.<br> Bayesian framework is a precise way of quantifying uncertainty. Hence, they give a way for the model to express its confidence in its outputs.

---

2.<br> Bayesian framework provides a way to prevent overfitting (by tracking the level of uncertainty involved) and is a means to generalise other methods for overfitting, such as regularisation and (more indirectly) dropout.


**SIDE NOTE**: How is regularisation generalised using a Bayesian framework? Regularisation adds a penalty with respect to some reference, thus biasing the model's weights toward a specific range of values. This can be generalised as a prior assumption about the distribution of the weights.

---

3.<br> Allows making the distinction between epistemic and aleatoric uncertainty.

- Epistemic uncertainty: Uncertainty due to lack of knowledge
- Aleatoric uncertainty: Uncertainty due to practically unaccountable factors

Philosophically, all uncertainty (at least with respect to mechanical phenomena) is epistemic, but in practice, many phenomena have too many factors to feasibly learn enough to overcome every aspect of uncertainty. A lot of models are unable to consider aleatoric uncertainty, which makes them overly confident about their predictions when it is clear they practically cannot be.

### Disadvantages of Bayesian approach in machine learning
1.<br> A neural network aims to generalise an unknown domain; this is often already a complex learning problem. Bayesian neural networks aim also to estimate the uncertainty they have about their predictions; this adds a layer of complexity on the learning problem. Furthermore, learning enough about an unknown domain to estimate uncertainty is epistemologically unreliable when using statistics alone.

---

2.<br> Making the implicit prior assumptions of a learning model explicit can be challenging.
