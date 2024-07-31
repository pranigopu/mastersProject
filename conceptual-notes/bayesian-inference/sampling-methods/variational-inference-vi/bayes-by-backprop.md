**BAYES-BY-BACKPROP**

**_"backprop" means "backpropagation"_**

---

**Contents**:

- [Introduction](#introduction)
- [Bayes-by-backprop algorithm](#bayes-by-backprop-algorithm)

---

> **Main resources**:
>
> - [_Hands-on Bayesian Neural Networks – A Tutorial for Deep Learning Users_](https://arxiv.org/pdf/2007.06823)
> - ["11.9.5. Variational Inference" from "11.9. Inference Methods" from _11. Appendiceal Topics_ from **Bayesian Computation Book**](https://bayesiancomputationbook.com/markdown/chp_11.html#variational-inference)

---

> **Main references**:
>
> - [_Bayes by Backprop_ from **Probabilitistic Deep Learning**](https://medium.com/neuralspace/probabilistic-deep-learning-bayes-by-backprop-c4a3de0d9743)

**NOTE**: _The following is my best attempt at understanding Bayes-by-backprop._

---

# Introduction
Bayes-by-backprop is a practical implementation of SVI combined with a reparametrisation trick to ensure backpropagation works as usual. The first key idea is to use $\epsilon \sim r(\epsilon)$ as a source of noise, wherein the distribution $r$ does not vary. The next key idea is to sample the model parameters $\theta$ not from the approximated posterior $q_{\phi}$ (which is a stochastic function) but from $t(\epsilon, \phi)$ (which is a deterministic function, with only the variable input $\epsilon$ being stochastic). Hence, $\theta \sim t(\epsilon, \phi)$. But the key point here is that $t$ must be defined such that $\theta$ (as sampled from $t$) follows $q_{\phi}$. Note also that $\epsilon$ is independent of $\phi$, which means during backpropagation, it can be considered constant, and its stochasticity does not affect the backpropagation process.

# Bayes-by-backprop algorithm
- $\phi = \phi_0$
- **for** $i=0$ to N do
    - Draw $\epsilon \sim q(\epsilon)$
    - $\theta = t(\epsilon, \phi)$
    - $f(\theta, \phi) = log(q\phi(\theta)) − log(p(D_y | D_x, \theta) p(\theta))$
    - $\Delta_\phi f = \text{backprop}_\phi(f)$
    - $\phi = \phi − \alpha \Delta_\phi f$
- **end for**

---

**NOTATION**:

- $f$: The objective function
- $\Delta_\phi$: Change with respect to change in $\phi$
- $D_x$: The training inputs
- $D_y$: The training labels