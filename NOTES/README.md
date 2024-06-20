**NOTES**

---

**Contents**:

- [Bayesian computation](#bayesian-computation)
    - [Advantages of Bayesian approach in machine learning](#advantages-of-bayesian-approach-in-machine-learning)
    - [Disadvantages of Bayesian approach in machine learning](#disadvantages-of-bayesian-approach-in-machine-learning)
- [Further reading](#further-reading)

---

# Bayesian computation
**_Especially in neural networks_**

## Advantages of Bayesian approach in machine learning
1.<br>

Bayesian framework is a precise way of quantifying uncertainty. Hence, they give a way for the model to express its confidence in its outputs.

2.<br>

Bayesian framework provides a way to prevent overfitting (by tracking the level of uncertainty involved) and is a means to generalise other methods for overfitting, such as regularisation and (more indirectly) dropout.

**SIDE NOTE**: _How is regularisation generalised using a Bayesian framework? Regularisation adds a penalty with respect to some reference, thus biasing the model's weights toward a specific range of values. This can be generalised as a prior assumption about the distribution of the weights._

3.<br>

Allows making the distinction between epistemic and aleatoric uncertainty.

- Epistemic uncertainty: Uncertainty due to lack of knowledge
- Aleatoric uncertainty: Uncertainty due to practically unaccountable factors

Philosophically, all uncertainty (at least with respect to mechanical phenomena) is epistemic, but in practice, many phenomena have too many factors to feasibly learn enough to overcome every aspect of uncertainty. A lot of models are unable to consider aleatoric uncertainty, which makes them overly confident about their predictions when it is clear they practically cannot be.

### Disadvantages of Bayesian approach in machine learning
1.<br>

A neural network aims to generalise an unknown domain; this is often already a complex learning problem. Bayesian neural networks aim also to estimate the uncertainty they have about their predictions; this adds a layer of complexity on the learning problem. Furthermore, learning enough about an unknown domain to estimate uncertainty is epistemologically unreliable when using statistics alone.

2.<br>

Making the implicit prior assumptions of a learning model explicit can be challenging.

# Further reading
- [Bayesian Inference (basics)](https://github.com/pranigopu/mastersProject/tree/main/NOTES/bayesian-inference)
- [Generative Models for Discrete Data](https://github.com/pranigopu/mastersProject/tree/main/NOTES/generative-models-for-discrete-data)
    - Draws on Bayesian inference (especially Bayesian modelling)
    - Explores Bayesian modelling for certain notable classes of problems involving discrete data
- [Markov Chains](https://github.com/pranigopu/mastersProject/tree/main/NOTES/markov-chains)
    - Necessary to understand computational approaches to Bayesian inference (e.g. for sampling from the posterior)
