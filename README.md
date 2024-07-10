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

**CONSIDER**: To compare BNNs in the context of RL or supervised learning?

While good benchmarks are available, and while BNNs can be used in the pipeline to support RL methods, the end result is opaque w.r.t. the performance of the BNNs themselves, i.e. the actual confidence of the BNN is abstracted away in the agent's performance. _Hence, it is an easier and more informative project to compare BNN methods in the context of supervised learning_, since the confidence of each BNN can be tested against new data to see how well they hold up.

**CONSIDER**: What does comparing BNN methods mean?

It means comparing Bayesian inference algorithms as applied to deep learning.

## Project resources
- Benchmark for testing reinforcement learning models (LESS RELEVANT)
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
- Posterior Sampling for Deep Reinforcement Learning (LESS RELEVANT)
    - https://arxiv.org/pdf/2305.00477.pdf
- Comparing BNNs for supervised learning problems (MORE RELEVANT)
    - https://www.alignmentforum.org/posts/79eegMp3EBs8ptFqa/neural-uncertainty-estimation-review-article-for-alignment
- Deep Bayesian Bandit Showdown (comparing BNNs in RL context) (LESS RELEVANT)
    - https://arxiv.org/pdf/1802.09127.pdf
- Benchmarking Bayesian Neural Networks and Evaluation Metrics for Regression Tasks (MORE RELEVANT)
    - https://arxiv.org/pdf/2206.06779.pdf
- (Wenzel et al., 2020a) (IMPORTANT)
    - https://arxiv.org/pdf/2102.06571
- https://udlbook.github.io/udlbook/ (check 159) (IMPORTANT)

Unidentified references: (Noci et al., 2021)
