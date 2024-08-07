<h1>NOTES</h1>

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
