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
      - [1. For regression problems](#1-for-regression-problems)
        - [1.1. Obtaining the estimator of the prediction](#11-obtaining-the-estimator-of-the-prediction)
        - [1.2. Summarising the uncertainty of the BNN](#12-summarising-the-uncertainty-of-the-bnn)
      - [2. For classification problems](#2-for-classification-problems)
        - [2.1. Obtaining the estimator of the prediction](#21-obtaining-the-estimator-of-the-prediction)
- [Advantages of using BNNs for deep learning](#advantages-of-using-bnns-for-deep-learning)
- [Bayesian inference algorithms](#bayesian-inference-algorithms)
  - [Markov chain Monte Carlo (MCMC)](#markov-chain-monte-carlo-mcmc)
  - [Variational inference (VI)](#variational-inference-vi)
  - [Bayes-by-backprop](#bayes-by-backprop)

---

# Abbreviations
- ML: Machine learning
- ANN: Artificial neural network
- BNN: Bayesian neural network (a kind of ANN)
- SNN: Stochastic neural network (a kind of ANN)
- MLE: Maximum likelihood estimation
- MAP: Maximum a posteriori (usually precedes "estimation")
- MCMC: Markov chain Monte Carlo
- NFLT: No free-lunch theorem for machine learning
- VI: Variational inference

> REFERENCES:
>
> - [No free-lunch theorem for machine learning](https://machinelearningmastery.com/no-free-lunch-theorem-for-machine-learning/)

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

**Stochastic neural networks (SNNs)** are a type of ANN built by introducing stochastic components into the network. This is performed by giving the network either a stochastic activation or stochastic weights to simulate multiple possible models $\theta$ with their associated probability distribution $P(\theta)$. Thus, BNNs can be considered a special case of ensemble learning.

_Ensemble learning to SNNs_...

The main motivation behind ensemble learning is that aggregating the predictions of a large set of average-performing but independent models can lead to better predictions than one well-performing expert model. SNNs may perform better than their point estimate counterparts for a similar reason, but a better performance is not the main aim of SNNs. Rather, the main aim of using an SNN architecture is to grasp the uncertainty about the underlying processes.

This is accomplished by comparing the predictions of multiple sampled models (based on multiple sampled parametrizations, i.e. multiple sampled values of $\theta$). If models agree, then the uncertainty rises. If models disagree, then the uncertainty falls. This process can be summarized as follows:

$\theta ∼ P(\theta)$ (prior distribution)

$y = \Phi_\theta(x) + \epsilon$ (regression with stochastic function $\Phi_\theta(x)$ )

**NOTE**: _As with all regression problems, we use the error term_ $\epsilon$ _to represent random noise that accounts for the fact that the function_ $\Phi$ _is only an approximation._

A BNN can then be defined as any SNN trained using Bayesian inference.

## Steps to design BNNs
1.<br>

Choice of deep neural network architecture, i.e. a functional model.

2.<br>

Choice of stochastic model, which consists of the following:

- $P(\theta)$: Prior distribution over the possible model parametrization
- $P(y|x, \theta)$: Prior confidence in the predictive power of the model 

Also, note that:

- The model parametrization can be considered to be the hypothesis $H$
- The training set is the data $D$
- $\theta$ can be a single value, a vector or a matrix

**CONSIDER**: _The choice of a BNN's stochastic model is analogous to the choice of loss function when training a point-estimation ANN._

## Additional points
**ANN cost function in statistical terms**:

The cost function is often defined as the log likelihood of the training set, sometimes with a regularisation term included. From a statistician’s point of view, this is a maximum likelihood estimation (MLE), or a maximum a posteriori (MAP) estimation when regularisation is used.

# Training and applying BNNs
**NOTE**: _Here, we are only considering BNNs as discriminative models, not generative models._

## Finding the posterior
The Bayesian posterior for complex models such as ANNs is a high dimensional and highly non-convex probability distribution. This complexity makes computing it using standard sampling methods (e.g. accept-reject sampling) an intractable problem, especially because computing the evidence (i.e. the denominator of Bayes' formula) is difficult. To address this problem, two broad approaches have been introduced (each approach has various specific methods that implement it):

1. Markov chain Monte Carlo (MCMC)
2. Variational inference (VI)

## Predictions using BNNs
Note that our discussion of inputs, functions, regression and outputs is done in the context of neural networks. Hence, we have input layer with inputs $x$ and an output layer with outputs (can be one or more) $y$, with a function $\Phi_\theta$ mapping $x$ to $y$ using the weights of the neural network $\theta$. Here, it is key to note that $x$ and $y$ are vectors, while $\theta$ is a matrix that holds the weights of the neural network (they are stored as a matrix to preserve their position in the network).

### The marginal
Predictions using BNNs are made using probability distribution $P(y|x, D)$, called the marginal, which quantifies the model's uncertainty on a certain prediction $y$. Given the posterior distribution $P(\theta|D)$, the marginal is:

$\displaystyle P(y|x, D) = \int_\Theta P(y|x, \theta) P(\theta|D) d\theta$

---

However, in practice, $P(y|x, D)$ is sampled indirectly using $y = \Phi_\theta(x) + \epsilon$ (regression with stochastic function $\Phi_\theta(x)$); this equation was discussed previously in the section ["SNNs to BNNs"](#snns-to-bnns). Note that $\theta$ is sampled from the posterior $P(\theta|D)$. Hence, the predictions are sampled as follows:

- Define the posterior $P(\theta|D)$
- **for** $i=1$ to $N$
    - Draw $\theta_i \sim \(\theta|D)$
    - $y_i = \Phi_{\theta_i}(x)$
- **end for**
- **return** $Y = {y_1, y_2 ... y_N}, \Theta = {\theta_1, \theta_2 ... \theta_N}$

Hence, note that $Y$ is collection of samples from the marginal $P(y|x, D)$ and $\Theta$ is a collection of samples from the posterior $P(\theta|D)$. Also note (though it should be apparent) that $x$ is a vector (of specific inputs), each $y_i$ is a vector (of specific outputs, based on specific weights sampled from the posterior) and each $\theta_i$ is a matrix (of specific weights sampled from the posterior).

### Quantifying prediction uncertainty and obtaining prediction estimator
Usually, aggregates are computed on those samples to (1) obtain an estimator for the prediction $y$ — this estimator is denoted by $\hat{y}$ — and (2) summarise the uncertainty of the BNN.

#### 1. For regression problems
##### 1.1. Obtaining the estimator of the prediction

Most common approach is averaging the sampled predictions:

$\displaystyle \hat{y} = \frac{1}{N} \sum_{i=1}^{N} \Phi_{\theta_i}(x)$

**NOTE**:

##### 1.2. Summarising the uncertainty of the BNN

This can be done using the covariance matrix:

$\displaystyle S_{y|x, D} = \frac{1}{N-1} \sum_{i=1}^N (\Phi_{\theta_i}(x) - \hat{y}) (\Phi_{\theta_i}(x) - \hat{y})^T$

**NOTE**: _We are assuming that_ $\Phi_{\theta_i}(x) - \hat{y}$ _is a column vector._

#### 2. For classification problems
Here, $\Phi_\theta$ does not give a vector of outputs but rather a vector of probabilities $p$, each corresponding to the estimated probability of the respective label being the true label (for clarity, consider how the last layer of a classification network is defined). In other words, we define $p = \Phi_\theta(x) + \epsilon$. Note that $p$ is a vector wherein the index of each probability corresponds to the label.

##### 2.1. Obtaining the estimator of the prediction

Averaging the estimated probabilities:

$\displaystyle \hat{p} = \frac{1}{N} \sum_{i=1}^{N} \Phi_{\theta_i}(x)$

Obtaining the label (i.e. index) that maximises the above:

$\displaystyle \hat{y} = \text{arg}\max_i \hat{p}$ ($i$ represents the index)

**NOTE**: $\hat{p} = (p_1, p_2 ... p_k)$

# Advantages of using BNNs for deep learning

1. Bayesian methods provide a natural approach for quantifying uncertainty
2. BNNs allow distinguishing between epistemic and aleatoric uncertainty
3. NFLT $\implies$ any supervised learning algorithm includes an implicit prior
4. Bayesian paradigm enables the analysis of learning methods

---

**Expanding of the above**:

**Point 1**: Quantifying uncertainty helps prevent overconfidence and underconfidence, since well-quantified uncertainty would be more consistent with the observed errors than mere predictions.

**Point 2**: A BNN's ability to distinguish between epistemic uncertainty $p(θ|D)$ and aleatoric uncertainty $p(y|x, θ)$ means it can learn from a small dataset without overfitting, since at prediction time, points lying outside the training distribution are given high epistemic uncertainty instead of blindly giving a wrong prediction.

**Point 3**: Any supervised learning algorithm includes some implicit prior. Bayesian methods, when used correctly, will at least make the prior explicit, which would make the model less of a black box. In Bayesian deep learning, priors are often considered as soft constraints that are analogous to regularisation or data transformations such as data augmentation in traditional deep learning. In particular, most regularisation methods used for point estimate neural networks can be understood from a Bayesian perspective as setting a prior.

**Point 4**:  Many learning methods initially not presented as Bayesian can be implicitly understood as being approximate Bayesian (e.g. regularisation, ensembling, etc.). In fact, most of the BNNs used in practice rely on methods that are approximately or implicitly Bayesian, since the exact algorithms are too computationally expensive. **+ Consider**: _The Bayesian paradigm also provides a systematic framework to design new learning and regularisation strategies, even for point estimate models._

# Bayesian inference algorithms
## Markov chain Monte Carlo (MCMC)
A family of algorithms to sample from the exact posterior distribution.

- [My notes on MCMC](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods.md#markov-chain-monte-carlo-mcmc)

## Variational inference (VI)
A family of algorithms to sample from an approximate posterior distribution.

**NOTE**: _Computationally less intensive and more scalable than MCMC methods._

- [My notes on VI](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods.md#variational-inference-vi)

## Bayes-by-backprop
Bayes-by-backprop is a practical implementation of stochastic VI combined with a reparametrisation trick to ensure backpropagation works as usual. Hence, I have put it under the "Variational inference" section: [My notes on Bayes-by-backprop](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods.md#bayes-by-backprop).
