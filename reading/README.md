# Reading
This directory contains all the papers (or at least their links) relevant to my project in some way. This directory also contains my summaries of commentaries on them.

## Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

>> LINK: https://arxiv.org/abs/1911.08265

This paper introduces _MuZero_, a model-based RL algorithm that outperforms state-of-the-art RL algorithms (model-free algorithms, since model-based model-learning algorithms before this always underperformed in visually complex domains). Furthermore, _MuZero_ is also comparable in its performance to specialised planning algorithms that use a perfect model of the domain (ex. _AlphaGo_ for Go), despite itself using only a learned model.

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
- Comparison in state-representation: (Appendix A) "_AlphaGo Zero and AlphaZero use knowledge of the rules of the game in three places: (1) state transitions in the search tree, (2) actions available at each node of the search tree, (3) episode termination within the search tree. In MuZero, all of these have been replaced with the use of a_ **_single implicit model learned by a neural network._**"
- Training method: (3. _MuZero_ Algorithm) "_All parameters of the model are trained jointly to accurately match the policy, value, and reward, for every hypothetical step_ $k$, _to corresponding target values observed after_ $k$ _actual time-steps have elapsed._"
- Avoiding illegal actions: (Appendix A) _"The network rapidly learns not to predict actions that never occur in the trajectories it is trained on"_ (thus avoiding illegal actions)
- Appendix B explains the search process
    - _MuZero_ uses Monte Carlo tree search (MCTS) to estimate action-value function
    - Action-value function is used to improve the policy (by choosing actions that maximise action values)
