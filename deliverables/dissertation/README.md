# Dissertation 
## Change log
[26-10-2024] Corrected the mathematical formula in the technical explanation of Hamiltonian Monte Carlo.

**Old version**:

$\displaystyle - \frac{\delta}{\delta \theta} \log P(\theta|D) = - \frac{\delta}{\delta \theta} \log \frac{P(D|\theta)P(\theta)}{P(D)}$ (by Bayes' rule)

$\displaystyle = - \frac{\delta}{\delta \theta} (\log P(D|\theta) P(\theta) - P(D))$

$\displaystyle = - \frac{\delta}{\delta \theta} \log P(D|\theta) P(\theta) + \frac{\delta}{\delta \theta} P(D)$

$\displaystyle = - \frac{\delta}{\delta \theta} \log P(D|\theta) P(\theta)$ (since $P(D)$ is a constant)

**Updated version**:

$\displaystyle - \frac{\delta}{\delta \theta} \log P(\theta|D) = - \frac{\delta}{\delta \theta} \log \frac{P(D|\theta)P(\theta)}{P(D)}$ (by Bayes' rule)

$\displaystyle = - \frac{\delta}{\delta \theta} (\log P(D|\theta) P(\theta) - \log P(D))$

$\displaystyle = - \frac{\delta}{\delta \theta} \log P(D|\theta) P(\theta) + \frac{\delta}{\delta \theta} \log P(D)$

$\displaystyle = - \frac{\delta}{\delta \theta} \log P(D|\theta) P(\theta)$ (since $P(D)$ is a constant)
