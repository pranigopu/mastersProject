**NOTES** <br> **_Mastering Diverse Domains through World Models_**

---

**Contents**:

- [Introduction](#introduction)
- [Key points](#key-points)
- [Points to review](#points-to-review)
  - [Solving the dilemma of regularisation strength](#solving-the-dilemma-of-regularisation-strength)
  - [Ensuring that network outputs do not become near deterministic (how \& why)](#ensuring-that-network-outputs-do-not-become-near-deterministic-how--why)
  - [Solving the exploration-exploitation dilemma for both sparse \& dense reward environments](#solving-the-exploration-exploitation-dilemma-for-both-sparse--dense-reward-environments)
- [Comparisons to past works in general-purposes algorithms](#comparisons-to-past-works-in-general-purposes-algorithms)
- [Possible future investiations](#possible-future-investiations)

---

# Introduction
This paper introduces _DreamerV3_, a model-based RL algorithm that is able to perform well in diverse domains (even outperforming specialised models) without manual tuning of hyperparameters. While RL algorithms can solve tasks in diverse domains, they are limited by the resources and knowledge needed to tune them for new tasks. _DreamerV3_ overcomes this limitation by being able to learn in diverse domains with fixed hyperparameters. It is also able to adapt to sparse and dense reward environments as needed. Furthermore, as the scale of the model increases, _DreamerV3_'s final performance and data efficiency also increases monotonically, thereby making _DreamerV3_ both general and scalable.

# Key points
- Learning across diverse domains by transforming signal magnitudes through normalisation techniques
- Learning compact representations of sensory inputs using autoencoding
- World model as a recurrent state-space model (RSSM)
- Predictors trained: dynamics predictor, reward predictor, continue predictor
    - What is the purpose and structure of each?
- Symlog of expected loss used to train the reward predictor
    - How does symlog ensure small scale representation loss?
    - How does ensuring small scale representation loss help DreamerV3 adapt to different scales of reward?
 - Solving exploration-exploitatin dilemma using entropy regularizer
    - How are the difference scales of reward variance between sparse & dense reward environments handled?
    - How is exploration increased for sparse rewards but decreased for dense rewards?
    - What does "normalising returns" mean & why is it done?

# Points to review

## Solving the dilemma of regularisation strength
"_Previous world models require scaling the representation loss differently based on the visual complexity of the environment. Complex 3D environments contain details unnecessary for control and thus prompt a stronger regularizer to simplify the representations and make them more predictable. In 2D games, the background is often static and individual pixels may matter for the task, requiring a weak regularizer to perceive fine details. We find that combining free bits with a small scale for the representation loss resolve this dilemma, allowing for fixed hyperparameters across domains. Moreover, symlog predictions for the decoder unify the gradient scale of the prediction loss across environments, further stabilizing the trade-off with the representation loss._"

Question: What are free bits and what do they add to the factor of small scale representation loss?

## Ensuring that network outputs do not become near deterministic (how & why)
"_We occasionally observed spikes the in KL losses in earlier experiments, consistent with reports for deep variational autoencoders. To prevent this, we parameterize the categorical distributions of the encoder and dynamics predictor as mixtures of 1% uniform and 99% neural network output, making it impossible for them to become near deterministic and thus ensuring well-scaled KL losses_"

**NOTE**: The Kullback–Leibler (KL) divergence (also called relative entropy and I-divergence), is a type of statistical distance: a measure of how one probability distribution $P$ is different from a second, reference probability distribution $Q$. For further reference, click [here](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)

## Solving the exploration-exploitation dilemma for both sparse & dense reward environments
"_The actor network learns to choose actions that maximize returns while ensuring sufficient exploration through an entropy regularizer. However, the scale of this regularizer heavily depends on the scale and frequency of rewards in the environment, which has been a challenge for previous algorithms. Ideally, we would like the policy to explore quickly in the absence of nearby returns without sacrificing final performance under dense returns. To stabilize the scale of returns, we normalize them using moving statistics. For tasks with dense rewards, one can simply divide returns by their standard deviation, similar to previous work._

_However, when rewards are sparse, the return standard deviation is generally small and this approach would amplify the noise contained in near-zero returns, resulting in an overly deterministic policy that fails to explore. Therefore, we propose propose to scale down large returns without scaling up small returns. We implement this idea by dividing returns by their scale S, for which we discuss multiple choices below, but only if they exceed a minimum threshold of 1._"

# Comparisons to past works in general-purposes algorithms
- _PPO_ requires relatively little tuning but uses large amounts of experience due to its on-policy nature (?)
- _SAC_ is a popular choice for continuous control
    - Leverages experience replay for higher data-efficiency
    - However, in practice it requires tuning, especially (especially for the entropy scale hyperparameter)
    - Struggles with high-dimensional inputs
- _MuZero_ plans using a value prediction model
    - Has achieved high performance
    - However, uses complex algorithmic components such as MCTS with UCB exploration & prioritized replay
- _Gato_ fits one large model to expert demonstrations of multiple tasks
    - However, it is only applicable to tasks where expert data is available

In comparison, DreamerV3 masters a diverse range of environments trained with fixed hyperparameters and from scratch.

# Possible future investiations
- Training larger models to solve multiple tasks across overlapping domains
    - To see how far the scaling properties of _DreamerV3_ can extrapolate, larger models are needed
    - World models can potentially enable substantial transfer between tasks
