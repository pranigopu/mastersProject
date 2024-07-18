<h1>NOTES</h1>

**_Benchmarking Bayesian Neural Networks and Evaluation Metrics for Regression Tasks_**

---

**Contents**:

- [Abbreviations](#abbreviations)
- [My goals in reading this paper](#my-goals-in-reading-this-paper)
- [The "what"](#the-what)
  - [Bayesian neural networks used](#bayesian-neural-networks-used)
  - [Evaluation metrics](#evaluation-metrics)
      - [Validity of the confidence intervals](#validity-of-the-confidence-intervals)
      - [Distance to the HMC reference (weight and function space)](#distance-to-the-hmc-reference-weight-and-function-space)
      - [Distance to the target posterior (weight space)](#distance-to-the-target-posterior-weight-space)
      - [Similarities between the algorithms (weight and function space)](#similarities-between-the-algorithms-weight-and-function-space)
  - [Experimental setup](#experimental-setup)
    - [Regression tasks](#regression-tasks)
    - [Neural network architectures](#neural-network-architectures)
    - [Hyperparameters](#hyperparameters)
    - [HMC reference](#hmc-reference)

---

# Abbreviations
- MCMC: Markov chain Monte Carlo
- VI: Variational inference
- SGD: Stochastic gradient descent

# My goals in reading this paper
Understand how...

- ... BNNs can be compared experimentally
- ... a synthetic regression problem can be implemented <br> _This relates more directly to my particular project_
- ... different BNN methods may be implemented in code

To understand "how", I must understand "what", i.e. I must understand what are the authors of the paper doing before I can understand how their implementations relate to BNNs and synthetic regression problems. Hence, I shall focus first on understanding what was done and how, and then look at the implementations and try to figure out how to recreate them in some way.

# The "what"
## Bayesian neural networks used
**1. Markov chain Monte Carlo (MCMC)**:

Using the MCMC method of Hamiltonian Monte Carlo (HMC). Refresher for MCMC: MCMC methods generate a Markov chain whose stationary distribution is the target posterior distribution.

> Reference: Neal, R. e. a. Mcmc using hamiltonian dynamics. _Handbook of Markov chain Monte Carlo_, 2(11):2, 2011.

**2. Stochastic gradient MCMC**:

Using the stochastic gradient (1) Lagenvin dynamics (SGLD) and (2) Hamiltonian Monte Carlo (SGHMC). _Why use stochastic gradient MCMC?_ In order to alleviate the computational cost of classical MCMC methods, many efforts have been dedicated to the development of stochastic gradient MCMC methods. Here, the Metropolis-Hastings correction step is omitted and the gradient of the potential function is approximated by a stochastic, mini-batched, gradient. Despite being computationally more efficient than classical MCMC, stochastic gradient MCMC methods introduce asymptotic bias.

> References:
>
> - Welling, M. and Teh, Y. Bayesian learning via stochastic gradient langevin dynamics. In _Proceedings of the 28th international conference on machine learning (ICML-11)_, pp. 681–688. Citeseer, 2011.
> - Ahn, S., Korattikara, A., and Welling, M. Bayesian posterior sampling via stochastic gradient fisher scoring. _arXiv preprint arXiv:1206.6380_, 2012.
> - Ding, N., Fang, Y., Babbush, R., Chen, C., Skeel, R., and Neven, H. Bayesian sampling using stochastic gradient thermostats. _Advances in neural information processing systems_, 27, 2014.
> - Chen, T., Fox, E., and Guestrin, C. Stochastic gradient hamiltonian monte carlo. In _International conference on machine learning_, pp. 1683–1691, 2014
> - Ma, Y., Chen, T., and Fox, E. A complete recipe for stochastic gradient mcmc. _Advances in neural information processing systems_, 28, 2015.
> - Li, C., Chen, C., Carlson, D., and Carin, L. Preconditioned stochastic gradient langevin dynamics for deep neural networks. In _Thirtieth AAAI Conference on Artificial Intelligence_, 2016
> - Zhang, R., Li, C., Zhang, J., Chen, C., and Wilson, A. Cyclical stochastic gradient mcmc for bayesian deep learning. _arXiv preprint arXiv:1902.03932_, 2019.

**3. Gaussian approximations**:

Gaussian approximations considered: (1) SWAG, (2) Laplace approximation. The SWAG approximation is constructed by collecting values of the parameters along a SGD trajectory with a possibly high step size.

**4. Variational inference (VI)**:

Using the Monte Carlo dropout method.

> Reference: Gal, Y. and Ghahramani, Z. Dropout as a bayesian approximation: Representing model uncertainty in deep learning. In _international conference on machine learning_, pp. 1050–1059. PMLR, 2016.


**5. Deep ensembles**:

Consists in training several neural networks independently with random initializations, and gathering their predictions to obtain a mean prediction and uncertainties. References:

> References:
>
> - Lakshminarayanan, B., Pritzel, A., and Blundell, C. Simple and scalable predictive uncertainty estimation using deep ensembles. _Advances in neural information processing systems_, 30, 2017.
> - Fort, S., Hu, H., and Lakshminarayanan, B. Deep ensembles: A loss landscape perspective. _arXiv preprint arXiv:1912.02757_, 2019.

## Evaluation metrics
1. Validity of the confidence intervals
2. Distance to the HMC reference (weight and function space)
3. Distance to the target posterior (weight space)
4. Similarities between the algorithms (weight and function space)

#### Validity of the confidence intervals
The validity of the confidence intervals produced by an approximation method with **coverage probabilities**. There are several related notions of coverage probabilities such as:

- Prediction interval coverage probability
- Marginal coverage probability
- Conditional coverage probability

> Reference: Lin, Z., Trivedi, S., and Sun, J. Locally valid and discriminative prediction intervals for deep learning models. _Advances in Neural Information Processing Systems_, 34: 8378–8391, 2021.

#### Distance to the HMC reference (weight and function space)
Computing the maximum mean discrepancy (MMD) between each approximation and the approximation obtained via exhaustive HMC.

> Reference for MMD: Gretton, A., Borgwardt, K., Rasch, M., Scholkopf, B., and Smola, A. A kernel method for the two-sample-problem. _Advances in neural information processing systems_, 19, 2006.

#### Distance to the target posterior (weight space)
Assessing the performance of an approximation method by measuring a distance to the target posterior distribution.

#### Similarities between the algorithms (weight and function space)
We also use the maximum mean discrepancy (MMD) in order to establish possible similarities between the algorithms.

## Experimental setup
### Regression tasks
4 synthetic regression problems where the output is one-dimensional but the input may be one or multi-dimensional. Training and testing datasets are obtained. Each element $(X_i, Y_i)$ of the datasets are such that $Y_i = f(X_i) + \epsilon_i$, where $\epsilon_i \sim \text{Normal}(\theta, \sigma^2)$ and $i = 1, . . . , N$. The underlying latent regression function $f$ and the variance of the noise $\sigma$ are both known.

**Implementation details**: Appendix B

### Neural network architectures
A feed-forward neural network with ReLU activations is used as the basic model architecture through which different Bayesian methods can be applied. The number of parameters ranges from 2651 to 20501. A centered normalized Gaussian is used as the prior distribution for the weights in all the experiments. Note that for each training dataset, a MAP estimate is computed by training the neural network with an Adam optimiaer and an exponentially decaying learning rate.

**Implementation details**: Appendix C

### Hyperparameters
**Implementation details**: Appendix A.3

### HMC reference
For a given training dataset D, a reference sample is generated by Hamiltonian Monte Carlo (HMC) and subsequently used to evaluate the performance of the selected algorithms. 3 HMC chains of 200 iterations each are run. The first 100 iterations are discarded as burn-in, and perform 10000 leapfrogs steps. The step size is selected such that the Metropolis-Hastings acceptance rates are at least above 80% (note that HMC uses a Metropolis-Hastings acceptance rate).

