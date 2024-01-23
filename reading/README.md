# Reading
This directory contains all the papers (or at least their links) relevant to my project in some way. This directory also contains my summaries of commentaries on them.

## Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

> LINK: https://arxiv.org/abs/1911.08265

This paper introduces _MuZero_, a model-based RL algorithm that outperforms state-of-the-art RL algorithms (model-free algorithms, since model-based model-learning algorithms before this always underperformed in visually complex domains). Furthermore, _MuZero_ is also comparable in its performance to specialised planning algorithms that use a perfect model of the domain (ex. _AlphaGo_ for Go), despite using only a learned model.

### BUILDUP: Previous solutions to planning in visually complex domains
- Tree-based planning algorithms (lookahead search (LS))
    - Very successful for the domain of focus
    - Cannot adapt to new environments
    - Non-apaptability $\implies$ Unsuitability for complex dynamic environments<br> _(ex. in robotics, industrial control, intelligent assistant, etc.)_
- Model-based RL algorithms
    - More generalisable than LS
    - Struggle in visually complex environments
- Model-free RL algorithms
    - Estimating state-value function & policy without learning the environment
    - Estimation is done through repeated interaction without learning the environment's model
    - Underperform compared to LS (especially where precise & complex planning is needed)

### Arriving at _MuZero_
The reason model-based RL algorithms underperformed is because they relied on accuractely and precisely learning the whole environment; even small mistakes could compound over time, and complex environments needed unfeasibly many interactions to model to the required accuracy and precision. Model-free RL algorithms did better than model-based RL algorithms here because model-free methods were more efficient in reaching a clearer view of potential rewards, since they did not focus on computationally intensive environment modelling. The reason model-free RL algorithms underperformed compared to lookahead search planning was because only estimating overall rewards of a state or action from a state is insufficient in informing the agent about long-term potential of different sequences of actions.
<br><br>

Hence, it seems clear that learning accurate and precise modelling for long-term planning is the only way to perform as good as or better than lookahead planning methods. In this spirit, _MuZero_ builds on _AlphaGo_ with respect to (1) search and (2) search-based policy-iteration. _MuZero_ extends _AlphaGo_ by including a learned model in the training process; this extends _AlphaGo_ such that the agent can deal with single-agent domains and non-zero intermediate rewards. However, unlike previous model-based methods, _MuZero_ does not aim to accurately and precisely model the whole environment, but only an abstracted part of the environment that is relevant to long-term planning. In other words, there are no constraints with respect to how the environment's states and rules are represented, allowing the algorithm to work on any condensed, computationally efficient representation it can come up with.
<br><br>

**Relevant quotation from the paper**...

"_However, unlike traditional approaches to model-based RL, this internal state $s^k$ has no semantics of environment state attached to it – it is simply the hidden state of the overall model, and its sole purpose is to accurately predict relevant, future quantities: policies, values, and rewards._"

### Key points to look out for
- Appendix A compares _AlphaGo_ to _MuZero_
- Comparison in state-representation:<br>(Appendix A) "_AlphaGo Zero and AlphaZero use knowledge of the rules of the game in three places: (1) state transitions in the search tree, (2) actions available at each node of the search tree, (3) episode termination within the search tree. In MuZero, all of these have been replaced with the use of a_ **_single implicit model learned by a neural network._**"
- Training method:<br>(3. _MuZero_ Algorithm) "_All parameters of the model are trained jointly to accurately match the policy, value, and reward, for every hypothetical step_ $k$, _to corresponding target values observed after_ $k$ _actual time-steps have elapsed._"
- Avoiding illegal actions:<br>(Appendix A) _"The network rapidly learns not to predict actions that never occur in the trajectories it is trained on"_ (thus avoiding illegal actions)
- Appendix B explains the search process
    - _MuZero_ uses Monte Carlo tree search (MCTS) to estimate action-value function
    - Action-value function is used to improve the policy (by choosing actions that maximise action values)

## Mastering Diverse Domains through World Models

> LINK: https://arxiv.org/abs/2301.04104

This paper introduces _DreamerV3_, a model-based RL algorithm that is able to perform well in diverse domains (even outperforming specialised models) without manual tuning of hyperparameters. While RL algorithms can solve tasks in diverse domains, they are limited by the resources and knowledge needed to tune them for new tasks. _DreamerV3_ overcomes this limitation by being able to learn in diverse domains with fixed hyperparameters. It is also able to adapt to sparse and dense reward environments as needed. Furthermore, as the scale of the model increases, _DreamerV3_'s final performance and data efficiency also increases monotonically, thereby making _DreamerV3_ both general and scalable.

### Key points
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

### Points to review

#### Solving the dilemma of regularisation strength
"_Previous world models require scaling the representation loss differently based on the visual complexity of the environment. Complex 3D environments contain details unnecessary for control and thus prompt a stronger regularizer to simplify the representations and make them more predictable. In 2D games, the background is often static and individual pixels may matter for the task, requiring a weak regularizer to perceive fine details. We find that combining free bits with a small scale for the representation loss resolve this dilemma, allowing for fixed hyperparameters across domains. Moreover, symlog predictions for the decoder unify the gradient scale of the prediction loss across environments, further stabilizing the trade-off with the representation loss._"

Question: What are free bits and what do they add to the factor of small scale representation loss?

#### Ensuring that netork outputs do not become near deterministic (how & why)
"_We occasionally observed spikes the in KL losses in earlier experiments, consistent with reports for deep variational autoencoders. To prevent this, we parameterize the categorical distributions of the encoder and dynamics predictor as mixtures of 1% uniform and 99% neural network output, making it impossible for them to become near deterministic and thus ensuring well-scaled KL losses_"

**NOTE**: The Kullback–Leibler (KL) divergence (also called relative entropy and I-divergence), is a type of statistical distance: a measure of how one probability distribution $P$ is different from a second, reference probability distribution $Q$. For further reference, click [here](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)

#### Solving the exploration-exploitation dilemma for both sparse & dense reward environments
"_The actor network learns to choose actions that maximize returns while ensuring sufficient exploration through an entropy regularizer. However, the scale of this regularizer heavily depends on the scale and frequency of rewards in the environment, which has been a challenge for previous algorithms. Ideally, we would like the policy to explore quickly in the absence of nearby returns without sacrificing final performance under dense returns. To stabilize the scale of returns, we normalize them using moving statistics. For tasks with dense rewards, one can simply divide returns by their standard deviation, similar to previous work._

_However, when rewards are sparse, the return standard deviation is generally small and this approach would amplify the noise contained in near-zero returns, resulting in an overly deterministic policy that fails to explore. Therefore, we propose propose to scale down large returns without scaling up small returns. We implement this idea by dividing returns by their scale S, for which we discuss multiple choices below, but only if they exceed a minimum threshold of 1._"

### Comparisons to past works in general-purposes algorithms
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

### Possible future investiations
- Training larger models to solve multiple tasks across overlapping domains
    - To see how far the scaling properties of _DreamerV3_ can extrapolate, larger models are needed
    - World models can potentially enable substantial transfer between tasks
