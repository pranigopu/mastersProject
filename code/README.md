<h1> CODE FOR THE PROJECT </h1>

This directory contains the code used to reach the results presented in the final dissertation.

<h1> Additional resources </h1>

- [Markov Chain Monte Carlo in Python](https://towardsdatascience.com/markov-chain-monte-carlo-in-python-44f7e609be98)
- [`tfp.mcmc.HamiltonianMonteCarlo`](https://www.tensorflow.org/probability/api_docs/python/tfp/mcmc/HamiltonianMonteCarlo)
- [MCMC Training of Bayesian Neural Networks](https://www.youtube.com/watch?v=mlXHUBp2IsE&t=2869s)
- [`MCMC_from_scratch.ipynb` (Google Colab Notebook)](https://colab.research.google.com/drive/1YQBSfS1Nb8a9TAMsV1RjWsiErWqXLbrj#scrollTo=Cg6SOq3kiWPP)

---

---

<h1> NOTES </h1>

---

# Technical terms used
**Covariate**:

In statistics, researchers are often interested in understanding the relationship between one or more explanatory variables and a response variable. However, occasionally there may be other variables that can affect the response variable that are not of interest to researchers. These variables are known as covariates. More precisely, covariates are independent variables that affect a response variable, but are not of interest in a study.

> **Reference**: https://www.statology.org/covariate/


# Python modules, libraries and functions used
## `tqdm` library
`tqdm` is a Python module that wraps any iterable and displays a smart progress bar with remaining time estimation. It works on any platform, in any console or GUI, and supports IPython/Jupyter. `tqdm` derives from the Arabic word "taqaddum" (تقدّم) which can mean "progress".

> **Reference**: https://pypi.org/project/tqdm/

## `torch.nn.Module.apply(fn)`
Applies `fn` recursively to every submodule (as returned by `.children()`) as well as self. Typical use includes initialising the parameters of a model (for more on initialising module parameters, see:[`nn-init-doc`](https://pytorch.org/docs/stable/nn.init.html)).

> **Reference**: [Source code for `torch.nn.modules.module` (PyTorch documentation)](https://pytorch.org/docs/master/_modules/torch/nn/modules/module.html#Module.apply)

## `tf.compat.v1.enable_eager_execution()`
