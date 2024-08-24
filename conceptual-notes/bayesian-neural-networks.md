**BAYESIAN NEURAL NETWORKS (BNNs)**

---

**Contents**

- [References](#references)
- [Abbreviations](#abbreviations)
- [Notations](#notations)
- [Why bother with BNNs?](#why-bother-with-bnns)
- [SNNs to BNNs](#snns-to-bnns)
  - [Why bother with SNNs?](#why-bother-with-snns)
  - [What is an SNN?](#what-is-an-snn)
  - [Ensemble learning to SNNs to BNNs](#ensemble-learning-to-snns-to-bnns)
- [Steps to design BNNs](#steps-to-design-bnns)
- [Training and applying BNNs](#training-and-applying-bnns)
  - [Finding the posterior](#finding-the-posterior)
    - [BNN with HMC](#bnn-with-hmc)
  - [Predictions using BNNs](#predictions-using-bnns)
    - [The marginal](#the-marginal)
    - [Quantifying prediction uncertainty and obtaining prediction estimator](#quantifying-prediction-uncertainty-and-obtaining-prediction-estimator)
      - [1. For regression problems](#1-for-regression-problems)
        - [1.1. Obtaining the estimator of the prediction](#11-obtaining-the-estimator-of-the-prediction)
        - [1.2. Summarising the uncertainty of the BNN](#12-summarising-the-uncertainty-of-the-bnn)
      - [2. For classification problems](#2-for-classification-problems)
        - [2.1. Obtaining the estimator of the prediction](#21-obtaining-the-estimator-of-the-prediction)
- [Advantages of using BNNs for deep learning](#advantages-of-using-bnns-for-deep-learning)
- [Additional points](#additional-points)


---

# References
- [_Hands-on Bayesian Neural Networks – A Tutorial for Deep Learning Users_ by Laurent Valentin Jospin, Hamid Laga, Farid Boussaid, Wray Buntine and Mohammed Bennamoun](https://arxiv.org/pdf/2007.06823)

# Abbreviations
- ML: Machine learning
- ANN: Artificial neural network
- BNN: Bayesian neural network (a kind of ANN)
- DL: Deep learning
- SNN: Stochastic neural network (a kind of ANN)
- MLE: Maximum likelihood estimation
- MAP: Maximum a posteriori (usually precedes "estimation")
- MCMC: Markov chain Monte Carlo
- HMC: Hamiltonian Monte Carlo (a class of MCMC methods)
- NFLT: No free-lunch theorem for machine learning
- VI: Variational inference

> **Reference**: [No free-lunch theorem for machine learning](https://machinelearningmastery.com/no-free-lunch-theorem-for-machine-learning/)

# Notations
- $D_x$: Training inputs
- $D_y$: Training labels
- $D$: Training set, where $D = (D_x, D_y)$
- $\theta$: A specific value/set of values of the model parameter <br> _Represents a particular model under the generalised model_
- $\Theta$: The set of all hypothesised model parameter values

# Why bother with BNNs?
_A BNN is a SNN trained using Bayesian inference._

---

The relevance of the above shall become clearer after learning about SNNs.

---

A key point is that unlike traditional ANNs, the weights in a BNN are not fixed but stochastic, and more precisely, the weights are distributed in a specific distribution. Before training, this distribution is the prior distribution (which is how the weights are initialised before training), but during and after training using some form of Bayesian inference, this distribution is the posterior distribution.

Hence, the goal of training BNNs is to use Bayesian inference to find the posterior distribution by which the model's weights are distributed. Hence, note that unlike traditional ANNs, the predictions of a BNN are also stochastic, and more precisely, the predictions of a BNN are based on weights as sampled from the posterior distribution. Hence, the Bayesian inference in DL not only offers a way to quantify uncertainty in DL models (using the posterior and output distribution) but also provides a mathematical framework (i.e. using mathematics from Bayesian inference) to understand many regularisation techniques and learning strategies that are already used in classic DL.

# SNNs to BNNs
## Why bother with SNNs?
Traditional ANNs (i.e. ANNs used for point estimation):

- Tend to lack explainability, due to not being able to quantify its uncertainty
- May generalise poorly yet overconfidently for out-of-training data points

_SNNs are the most flexible solution to the above problems._

## What is an SNN?
An SNN is an ANN with stochastic components. More precisely, an SNN is an ANN with either stochastic activations or stochastic weights; thus, an SNN simulates a range of possible models $\theta$ with their associated probability distribution $P(\theta)$. Thus, SNNs can be considered a special case of ensemble learning

## Ensemble learning to SNNs to BNNs
The main motivation behind ensemble learning is that aggregating the predictions of a large set of average-performing but independent models can lead to more accurate and well-generalised predictions than one well-performing expert model. SNNs may lead to more accurate and well-generalised predictions than their point estimate counterparts for a similar reason, but improving the model's performance is not an SNN's primary aim.

The primary aim of using an SNN is to grasp the uncertainty about the underlying processes. This is done by comparing the predictions of multiple sampled models (based on multiple sampled parametrisations, i.e. multiple sampled values of $\theta$). If models agree, then the uncertainty falls. If models disagree, then the uncertainty rises. This process can be summarised as follows:

| Expression | Remark |
| --- | --- |
| $\theta \in \Theta$ | $\Theta$ is the set of all possible/considered models |
| $\theta ∼ P(\theta)$ | $P(\theta)$ is the probability distribution of models |
| $y = \Phi_\theta(x) + \epsilon$ | Regression with stochastic function $\Phi_\theta(x)$ |

---

**NOTES ON THE ABOVE**:

**1. Use of the error term** $\epsilon$:

- $\epsilon$ represents random noise in the real-world data generation being modelled
- Accounts for the fact that the function $\Phi_\theta$ is only an approximation

**2. The source of stochasticity in** $\Phi_\theta$:

Either one of the following:

- Stochastic activations of the neural network
- Stochastic weights of the neural network

**3. What** $\theta$ **represents**:

- The ordered set of all stochastic parameters of the neural network
- Usually denotes the ordered set of stochastic weights
- Can represent the parameters of the stochastic activations

---

Hence, we see that an SNN can be translated into a BNN context as follows:

| Expression | Remark |
| --- | --- |
| $\theta \in \Theta$ | $\Theta$ is the hypothesis space of the possible models |
| $\theta ∼ P(\theta)$ | $P(\theta)$ is the prior distribution over the possible models |
| $y = \Phi_\theta(x) + \epsilon$ | Model output for input $x$ |

---

**LEXICAL NOTE: "Model" vs. "generalised model"**:

Usually, when talking of "models", I talk about a particular architecture with a particular parametrisation. However, I may also talk about model in the sense of a generalised model, i.e. a particular architecture with a range of possible parametrisations. To avoid ambiguity, when I say "model", I only mean a particular architecture with a particular parametrisation, and when I want to refer to a generalised model, I will refer to it as a "generalised model" and nothing else. Hence, note that when I talk about "possible models", I am talking about the "possible parametrisations of a generalised model".

**Why do I make such a distinction?**

Theoretical analysis often distinguishes between the hypothesis class and specific hypotheses. For example, in DL, the term "model" may be used to refer to both the neural network's architecture (hypothesis class) and a particular parametrisation of a particular architecture meant to generalise over a particular set of inputs (specific hypothesis). Hence, to retain such a distinction while also retaining the broader conceptual link, I distinguish between "generalised model" and "model".

**NOTE**: _Referring to the hypothesis class and the specific hypothesis as "models" is not invalid, because a model is an abstraction of a process designed to represent the process within a given context, and thus, both a hypothesis class and a specific hypothesis are in fact models in their respective contexts. But for the sake of clarity, I shall be using "model" to refer to a specific hypothesis and "generalised model" to refer to a hypothesis class._

# Steps to design BNNs
1.<br>

Choice of deep neural network architecture, i.e. a functional model.

**NOTE**: _This helps define the hypothesis class, i.e. the generalised model._

2.<br>

Choice of stochastic model, which consists of the following:

- $P(\theta)$: Prior distribution over the possible models
- $P(y|x, \theta)$: Prior confidence in the predictive power of the model 

---

**NOTE**:

- Each model is a specific hypothesis $h$ in a hypothesis space $H$
- The training set is the data $D$
- $\theta$ can be a single value, a vector or a matrix
- In a neural network, $\theta$ is a vector or a matrix (usually the latter)

# Training and applying BNNs
**NOTE**: _Here, we are only considering BNNs as discriminative models, not generative models._

## Finding the posterior
The Bayesian posterior for complex models such as ANNs is a high dimensional and highly non-convex probability distribution. This complexity makes computing it using standard sampling methods (e.g. accept-reject sampling) an intractable problem, especially because computing the evidence (i.e. the denominator of Bayes' formula) is difficult. To address this problem, two broad approaches have been introduced (each approach has various specific methods that implement it): (1) MCMC and (2) VI.

> **Reference for a conceptual understanding of the sampling methods**:
> 
> 1. [Markov chain Monte Carlo (MCMC)](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/markov-chain-monte-carlo-mcmc)
> 2. [Variational inference (VI)](https://github.com/pranigopu/mastersProject/blob/main/conceptual-notes/bayesian-inference/sampling-methods/variational-inference-vi)

However, while the above references give a conceptual understanding of the sampling methods, it is not clear how these methods can be used to train a BNN. This shall be the focus of the next few sections, specifically for: Hamiltonian Monte Carlo (HMC, a class of MCMC methods).

### BNN with HMC
> **Reference**: [_Training BNNs with HMC_ from **janosh.dev**](https://janosh.dev/posts/hmc-bnn)



> **Additional reference (unused)**: [_Hamiltonian Monte Carlo Methods in Machine Learning_ by Tshilidzi Marwala, Wilson Tsakane Mongwe and Rendani Mbuvha](https://www.sciencedirect.com/book/9780443190353/hamiltonian-monte-carlo-methods-in-machine-learning)

## Predictions using BNNs
Note that our discussion of inputs, functions, regression and outputs is done in the context of neural networks. Hence, we have input layer with inputs $x$ and an output layer with outputs (can be one or more) $y$, with a function $\Phi_\theta$ mapping $x$ to $y$ using the weights of the neural network $\theta$. Here, it is key to note that $x$ and $y$ are vectors, while $\theta$ is a matrix that holds the weights of the neural network (they are stored as a matrix to preserve their position in the network).

### The marginal
Predictions using BNNs are made using probability distribution $P(y|x, D)$, called the marginal, which quantifies the model's uncertainty on a certain prediction $y$. Given the posterior distribution $P(\theta|D)$, the marginal is:

$\displaystyle P(y|x, D) = \int_\Theta P(y|x, \theta) P(\theta|D) d\theta$

---

However, in practice, $P(y|x, D)$ is sampled indirectly using $y = \Phi_\theta(x) + \epsilon$ (regression with stochastic function $\Phi_\theta(x)$); this equation was discussed previously in the section ["SNNs to BNNs"](#snns-to-bnns). Note that $\theta$ is sampled from the posterior $P(\theta|D)$. Hence, the predictions are sampled as follows:

- Define the posterior $P(\theta|D)$
- **for** $i=1$ to $N$
    - Draw $\theta_i \sim (\theta|D)$
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

# Additional points
**ANN cost function in statistical terms**:

The cost function is often defined as the log likelihood of the training set, sometimes with a regularisation term included. From a statistician’s point of view, this is a maximum likelihood estimation (MLE), or a maximum a posteriori (MAP) estimation when regularisation is used.