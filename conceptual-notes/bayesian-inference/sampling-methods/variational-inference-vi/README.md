**VARIATIONAL INFERENCE (VI)**

---

**Contents**:

- [Motivation](#motivation)
- [Conceptual introduction](#conceptual-introduction)
- [Theoretical foundations](#theoretical-foundations)
- [Further reading: Practical implementation](#further-reading-practical-implementation)

---

> **Main resources**:
>
> - [_Hands-on Bayesian Neural Networks – A Tutorial for Deep Learning Users_](https://arxiv.org/pdf/2007.06823)
> - ["11.9.5. Variational Inference" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Book**](https://bayesiancomputationbook.com/markdown/chp_11.html#variational-inference)

---

# Motivation
MCMC algorithms are the best tools for sampling from the exact posterior. However, their lack of scalability has made them less popular for BNNs, given the size of the models under consideration. Compared to MCMC, variational inference tends to be easier to scale to large data and is faster to run computationally, but with less theoretical guarantees of convergence.

# Conceptual introduction
Variational inference is not an exact method. Rather than allowing sampling from the exact posterior, the idea is to have a distribution $q_\phi(\theta)$, called the variational distribution, parametrized by a set of parameters $\phi$. The values of the parameters $\phi$ are then learned such that the variational distribution $q_\phi(\theta)$ is as close as possible to the exact posterior $p(\theta|D)$. The measure of closeness that is commonly used is the Kullback-Leibler divergence (KL-divergence). In practice we usually choose $q$ to be of simpler form than $p$, and we find the member of $q$'s family of distributions that is the closest to the target distribution $p$ (the closeness being commonly measured by the KL divergence), using optimization.

# Theoretical foundations
**NOTATION**:

$\Theta$ denotes the entire hypothesis space. $E$ denotes "expectation" (computed by the theoretical mean). $E_\theta$ denotes marginal expectation with respect to $\theta$. Note that marginal expectation with respect to $\theta$ is the expectation where everything apart from $\theta$ is kept constant (i.e. $\theta$, which represents the hypothesised model, is kept variable, while $D$, which represents the observed data, is kept constant).

**NOTE**: _The goal is to minimise the KL-divergence._

---

KL-divergence between $p$ and $q$ is given by:

$KL(q_\phi(\theta) || p(\theta|D))$

$= E_\theta(\log q_\phi(\theta) - \log p(\theta|D))$

$\displaystyle = E_\theta(\log \frac{q_\phi(\theta)}{p(\theta|D)})$

$\displaystyle = \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta)}{p(\theta|D)} d\theta$

---

Now, note that:

$p(\theta, D) = p(\theta|D) p(D)$

$\displaystyle \implies p(\theta|D) = \frac{p(\theta, D)}{p(D)}$

---

Hence, we have that:

$KL(q_\phi(\theta) || p(\theta|D))$

$\displaystyle = \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta) p(D)}{p(\theta, D)} d\theta$

$\displaystyle = p(D) \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta)}{p(\theta, D)} d\theta$

---

Now, note that $p(D)$ is constant with respect to $q_\phi(\theta)$.

Hence, here, $p(D)$ is irrelevant in minimising the KL-divergence.

Hence, here, minimising the KL-divergence means minimising:

$\displaystyle \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{q_\phi(\theta)}{p(\theta, D)} d\theta$

$\displaystyle = E_\theta(\log \frac{q_\phi(\theta)}{p(\theta, D)})$

$= E_\theta(\log q_\phi(\theta) - \log p(\theta, D))$

$= E_\theta(\log q_\phi(\theta)) - E_\theta(\log p(\theta, D))$

---

Minimising the above is the same as maximising the following:

$E_\theta(\log p(\theta, D)) - E_\theta(\log q_\phi(\theta))$

$= E_\theta(\log p(\theta, D) - \log q_\phi(\theta))$

$\displaystyle = E_\theta(\log \frac{p(\theta, D)}{q_\phi(\theta)})$

$\displaystyle = \int_{\theta \in \Theta} q_\phi(\theta) \log \frac{p(\theta, D)}{q_\phi(\theta)} d\theta$

The above is called the evidence lower bound, i.e. **ELBO**. The ELBO is easier to compute, and maximising the ELBO achieves the same optimisation as minimising the KL-divergence. Of course, the last integral above must be computed, and practically, it is usually computed through approximate methods, such as averaging Monte Carlo samples drawn from the surrogate distribution $q_\phi(\theta)$ and plugging them into the ELBO formula.

# Further reading: Practical implementation
Note that VI presents a machine learning optimisation problem, where we have a set of one or more parameters, namely $\phi$ (that defines the approximated posterior $q_\phi$), and an objective function, namely ELBO. The most popular method to optimise the ELBO is stochastic VI (SVI), which is in fact the stochastic gradient descent method applied to VI. Now, note that while VI offers a good mathematical tool for Bayesian inference, it needs to be adapted to deep learning. The main problem is that stochasticity stops backpropagation from functioning at the internal nodes of a network. Solutions to mitigate this problem include:

- [Bayes-by-backprop](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/variational-inference-vi/bayes-by-backprop.md)
- Probabilistic backpropagation