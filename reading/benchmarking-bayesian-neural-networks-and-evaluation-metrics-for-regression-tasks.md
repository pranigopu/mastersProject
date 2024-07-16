<h1>NOTES</h1>

**_Benchmarking Bayesian Neural Networks and Evaluation Metrics for Regression Tasks_**

---

**Contents**:

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

# Bayesian neural networks used
**1. Markov chain Monte Carlo (MCMC)**:

Using the MCMC method of Hamiltonian Monte Carlo (HMC). Refresher for MCMC: MCMC methods generate a Markov chain whose stationary distribution is the target posterior distribution. Reference: Neal, R. e. a. Mcmc using hamiltonian dynamics. _Handbook of Markov chain Monte Carlo_, 2(11):2, 2011.

**2. Stochastic gradient MCMC**:

Using the stochastic gradient (1) Lagenvin dynamics (SGLD) and (2) Hamiltonian Monte Carlo (SGHMC). _Why use stochastic gradient MCMC?_ In order to alleviate the computational cost of classical MCMC methods, many efforts have been dedicated to the development of stochastic gradient MCMC methods. Here, the Metropolis-Hastings correction step is omitted and the gradient of the potential function is approximated by a stochastic, mini-batched, gradient. Despite being computationally more efficient than classical MCMC, stochastic gradient MCMC methods introduce asymptotic bias. References:

- Welling, M. and Teh, Y. Bayesian learning via stochastic gradient langevin dynamics. In _Proceedings of the 28th international conference on machine learning (ICML-11)_, pp. 681–688. Citeseer, 2011.
- Ahn, S., Korattikara, A., and Welling, M. Bayesian posterior sampling via stochastic gradient fisher scoring. _arXiv preprint arXiv:1206.6380_, 2012.
- Ding, N., Fang, Y., Babbush, R., Chen, C., Skeel, R., and Neven, H. Bayesian sampling using stochastic gradient thermostats. _Advances in neural information processing systems_, 27, 2014.
- Chen, T., Fox, E., and Guestrin, C. Stochastic gradient hamiltonian monte carlo. In _International conference on machine learning_, pp. 1683–1691, 2014
- Ma, Y., Chen, T., and Fox, E. A complete recipe for stochastic gradient mcmc. _Advances in neural information processing systems_, 28, 2015.
- Li, C., Chen, C., Carlson, D., and Carin, L. Preconditioned stochastic gradient langevin dynamics for deep neural networks. In _Thirtieth AAAI Conference on Artificial Intelligence_, 2016
- Zhang, R., Li, C., Zhang, J., Chen, C., and Wilson, A. Cyclical stochastic gradient mcmc for bayesian deep learning. _arXiv preprint arXiv:1902.03932_, 2019.

**3. Gaussian approximations**:

Gaussian approximations considered: (1) SWAG, (2) Laplace approximation. The SWAG approximation is constructed by collecting values of the parameters along a SGD trajectory with a possibly high step size.

**4. Variational inference (VI)**:

Using the Monte Carlo dropout method. Reference: Gal, Y. and Ghahramani, Z. Dropout as a bayesian approximation: Representing model uncertainty in deep learning. In _international conference on machine learning_, pp. 1050–1059. PMLR, 2016.


**5. Deep ensembles**:

Consists in training several neural networks independently with random initializations, and gathering their predictions to obtain a mean prediction and uncertainties. References:

- Lakshminarayanan, B., Pritzel, A., and Blundell, C. Simple and scalable predictive uncertainty estimation using deep ensembles. _Advances in neural information processing systems_, 30, 2017.
- Fort, S., Hu, H., and Lakshminarayanan, B. Deep ensembles: A loss landscape perspective. _arXiv preprint arXiv:1912.02757_, 2019.
