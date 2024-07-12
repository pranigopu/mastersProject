<h1>NOTES</h1>

**_Hands-on Bayesian Neural Networks – A Tutorial for Deep Learning Users_**

---

**Contents**:

- [Abbreviations](#abbreviations)
- [Notations](#notations)
- [Basics of a BNN](#basics-of-a-bnn)
  - [SNNs to BNNs](#snns-to-bnns)
  - [Steps to design BNNs](#steps-to-design-bnns)
  - [Additional points](#additional-points)
- [Training and applying BNNs](#training-and-applying-bnns)
  - [Finding the posterior](#finding-the-posterior)
  - [Predictions using BNNs](#predictions-using-bnns)
    - [The marginal](#the-marginal)
    - [Quantifying prediction uncertainty and obtaining prediction estimator](#quantifying-prediction-uncertainty-and-obtaining-prediction-estimator)
      - [For regression problems](#for-regression-problems)

---

# Abbreviations
- ANN: Artificial neural network
- BNN: Bayesian neural network (a kind of ANN)
- SNN: Stochastic neural network (a kind of ANN)
- MLE: Maximum likelihood estimation
- MAP: Maximum a posteriori (usually precedes "estimation")
- MCMC: Markov chain Monte Carlo
- VI: Variational inference

# Notations
- $D_x$: Training inputs
- $D_y$: Training labels
- $D$: Training set, where $D = (D_x, D_y)$
- $\theta$: A specific value/set of values of the model parameter <br> _Represents a particular model under the generalised model_
- $\Theta$: The set of all hypothesised model parameter values

# Basics of a BNN
Using Bayes' formula to train a model can be understood as learning from the data $D$. Hence, the Bayesian paradigm not only offers a way to quantify uncertainty in deep learning models but also provides a mathematical framework to understand many regularisation techniques and learning strategies that are already used in classic deep learning. BNN is a stochastic artificial neural network trained using Bayesian inference.

## SNNs to BNNs
The point estimate approach, which is the traditional approach in deep learning, is relatively easy to deploy with modern algorithms and software packages, but tends to lack explainability. The final model might also generalize in unforeseen and overconfident ways on out-of-training distribution data points. This property, in addition to the inability of ANNs to say “I don’t know”, is problematic for many critical applications. Of all the techniques that exist to mitigate this, stochastic neural networks have proven to be one of the most generic and flexible.

**Stochastic neural networks (SNNs)** are a type of ANN built by introducing stochastic components into the network. This is performed by giving the network either a stochastic activation or stochastic weights to simulate multiple possible models $\theta$ with their associated probability distribution $p(\theta)$. Thus, BNNs can be considered a special case of ensemble learning.

_Ensemble learning to SNNs_...

The main motivation behind ensemble learning is that aggregating the predictions of a large set of average-performing but independent models can lead to better predictions than one well-performing expert model. SNNs may perform better than their point estimate counterparts for a similar reason, but a better performance is not the main aim of SNNs. Rather, the main aim of using an SNN architecture is to grasp the uncertainty about the underlying processes.

This is accomplished by comparing the predictions of multiple sampled models (based on multiple sampled parametrizations, i.e. multiple sampled values of $\theta$). If models agree, then the uncertainty rises. If models disagree, then the uncertainty falls. This process can be summarized as follows:

$\theta ∼ p(\theta)$ (prior distribution)

$y = \Phi_\theta(x) + \epsilon$ (regression with stochastic function $\Phi_\theta(x)$)

**NOTE**: _As with all regression problems, we use the error term_ $\epsilon$ _to represent random noise that accounts for the fact that the function_ $\Phi$ _is only an approximation._

A BNN can then be defined as any SNN trained using Bayesian inference.

## Steps to design BNNs
1.<br>

Choice of deep neural network architecture, i.e. a functional model.

2.<br>

Choice of stochastic model, which consists of the following:

- $p(\theta)$: Prior distribution over the possible model parametrization
- $p(y|x, \theta)$: Prior confidence in the predictive power of the model 

Also, note that:

- The model parametrization can be considered to be the hypothesis $H$
- The training set is the data $D$

**CONSIDER**: _The choice of a BNN's stochastic model is analogous to the choice of loss function when training a point-estimation ANN._

## Additional points
**ANN cost function in statistical terms**:

The cost function is often defined as the log likelihood of the training set, sometimes with a regularisation term included. From a statistician’s point of view, this is a maximum likelihood estimation (MLE), or a maximum a posteriori (MAP) estimation when regularisation is used.

# Training and applying BNNs
## Finding the posterior
The Bayesian posterior for complex models such as ANNs is a high dimensional and highly non-convex probability distribution. This complexity makes computing it using standard sampling methods (e.g. accept-reject sampling) an intractable problem, especially because computing the evidence (i.e. the denominator of Bayes' formula) is difficult. To address this problem, two broad approaches have been introduced (each approach has various specific methods that implement it):

1. Markov chain Monte Carlo (MCMC)
2. Variational inference (VI)

## Predictions using BNNs
### The marginal
Predictions using BNNs are made using probability distribution $p(y|x, D)$, called the marginal, which quantifies the model's uncertainty on a certain prediction $y$. Given the posterior distribution $p(\theta|D)$, the marginal is:

$\displaystyle p(y|x, D) = \int_\Theta p(y|x, \theta) p(\theta|D) d\theta$

---

However, in practice, $p(y|x, D)$ is sampled indirectly using $y = \Phi_\theta(x) + \epsilon$ (regression with stochastic function $\Phi_\theta(x)$); this equation was discussed previously in the section ["SNNs to BNNs"](#snns-to-bnns). Note that $\theta$ is sampled from the posterior $p(\theta|D)$. Hence, the predictions are sampled as follows:

- Define the posterior $p(\theta|D)$
- **for** $i=1$ to $N$
    - Draw $\theta_i \sim \(\theta|D)$
    - $y_i = \Phi_{\theta_i}(x)$
- **end for**
- **return** $Y = {y_1, y_2 ... y_N}, \Theta = {\theta_1, \theta_2 ... \theta_N}$

Hence, note that $Y$ is collection of samples from the marginal $p(y|x, D)$ and $\Theta$ is a collection of samples from the posterior $p(\theta|D)$.

### Quantifying prediction uncertainty and obtaining prediction estimator
Usually, aggregates are computed on those samples to (1) obtain an estimator for the prediction $y$ — this estimator is denoted by $\hat{y}$ — and (2) summarise the uncertainty of the BNN.

#### For regression problems
**1. Obtaining the estimator of the prediction**:

Most common approach is averaging the sampled predictions:

$\displaystyle \hat{y} = \frac{1}{N} \sum_{i=1}^{N} \Phi_{\theta_i}(x)$

**NOTE**:

**2. Summarising the uncertainty of the BNN**:

This can be done using the covariance matrix:

