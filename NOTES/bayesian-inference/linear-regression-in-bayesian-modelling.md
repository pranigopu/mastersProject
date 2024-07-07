**LINEAR REGRESSION IN BAYESIAN MODELLING**

---

**Contents**:

- [Basic scenario](#basic-scenario)
- [Extending the basic scenario](#extending-the-basic-scenario)

---

# Basic scenario
Consider the following scenario:

- Observed data $y={y_1, y_2 ... y_n}$
- Model parameters $\theta$
- Likelihood $P(y|\theta)$
- Let $Y$ be the random variable that generalises $y$

Now, consider that $Y$ depends linearly on independent variables $X = (X_1, X_2 ... X_k)$. Hence, we can model $Y$ using a linear regression model. More precisely, we have that $y_i = w_1 x_{1,i} + w_2 x_{2,i} ... w_k x_{k,i} = w^T x_i$, where $w$ is the column vector of coefficients $w_1, w_2 ... w_k$ and $x_i$ is the column vector of the $i$-th observation of independent variables $X_1, X_2 ... X_k$. Let $x = (x_1, x_2 ... x_n)$, where each $x_i$ is as before, i.e. the column vector for the $i$-th observation of the independent variable's values. In such a case, we get the following linear regression model:

$P(y|x, \theta) = \text{Normal}(y|w^Tx, \sigma)$

**NOTE** $w^Tx$ _is a single value._

Hence, we get the following (putting $\mu = w^Tx$ for convenience):

- $Y$ is normally distributed, with parameters $\theta = (\mu, \sigma)$
- Hence, likelihood is $P(Y|\theta) = \text{Normal}(Y|\mu, \sigma)$
- Also, we have some prior $P(\mu, \sigma)$ distributing the parameters

**NOTE**: _Though_ $x$ _is given,_ $w$ _is not, making_ $w^Tx$ _a single variable parameter_.

Hence, the posterior is as follows:

$P(\mu, \sigma|y) \propto \text{Normal}(Y|\mu, \sigma) P(\mu, \sigma)$

i.e. $P(w^Tx, \sigma|y) \propto \text{Normal}(Y|w^Tx, \sigma) P(w^Tx, \sigma)$

---

Using the posterior distribution adds to the usual linear regression model-fitting approach by conveying the level of uncertainty we have about our fitted model as well as other potential models. After all, a fitted model is only an estimate and may not reflect the true relationship between the outcome variable $Y$ and the independent variables $X_1, X_2 ... X_k$.

# Extending the basic scenario
To model non-linear relationshipps, replace $X$ (taking it as a single random variable, rather than a tuple of random variables as defined before) with some non-linear function of inputs $\phi : \mathbb(R) \rightarrow \mathbb(R)^d$, where $d$ is some constant. For example, we could have $\phi$ such that $\phi(x) = (1, x^2, x^3 ... x^d)$. In such a case, the linear regression model would be as follows (the Bayesian modelling would change accordingly):

$P(y|x, \theta) = \text{Normal}(y|w^T\phi(x), \sigma)$

**NOTE**: _The above is still linear with respect to_ $w$, _hence it is still linear regression._