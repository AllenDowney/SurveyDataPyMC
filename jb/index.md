---
myst:
  html_meta:
    description: "A tutorial on Bayesian regression in Python with PyMC: logistic, categorical, and ordinal models of General Social Survey data."
og:description: "A tutorial on Bayesian regression in Python with PyMC: logistic, categorical, and ordinal models of General Social Survey data."
---

# Bayesian Regression for Survey Data with PyMC

[Allen Downey](https://allendowney.com) and [Alexander Fengler](https://github.com/AlexanderFengler)

In this tutorial, we explore Bayesian regression using PyMC -- the primary library for Bayesian sampling in Python -- focusing on survey data and other datasets with categorical outcomes. Starting with logistic regression, we'll build up to categorical and ordered logistic regression, showcasing how Bayesian approaches provide versatile tools for developing and evaluating complex models. Participants will leave with practical skills for implementing Bayesian regression models in PyMC, along with a deeper appreciation for the power of Bayesian inference in real-world data analysis.

The examples use data from the [General Social Survey](https://gss.norc.org/) (GSS). We presented this tutorial at ODSC East 2025. Its companion, [Survey Data with Pandas](https://allendowney.github.io/SurveyDataPandas/), uses the same GSS data.

**Level:** intermediate. You should be comfortable with Python, NumPy and pandas, and basic statistics. You don't need any experience with Bayesian methods or PyMC.

**Length:** about 90 minutes.

## The notebooks

The pages on this site show the notebooks with solutions; click on a hidden cell to see it. To do the exercises, run the versions with blanks on Colab:

* [Introduction to Bayesian sampling](00_intro): using PyMC as a random number generator, then building up a model from an uncertain probability, a latent propensity, and observed data. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/00_intro.ipynb)

* [Logistic regression](01_logistic_regression): whether people say other people can be trusted, as a function of time and political party. Priors, the posterior distribution, sampling diagnostics, centering, and predictions. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/01_logistic_regression.ipynb)

* [Categorical regression](02_categorical_regression): the 2020 presidential vote as a function of age and gender. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/02_categorical_regression.ipynb)

* [Ordinal regression](03_ordinal_regression): how happy people say they are, as a function of age and birth cohort. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/03_ordinal_regression.ipynb)

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vSjMfp2TotFMnfpqoefutAEGue3p94qmbSshnnyZH0cs6o33JiGiSH5FxRPQ9qO30G12HDIhQI-vQkH/pub).

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. The notebooks install [nutpie](https://github.com/pymc-devs/nutpie), the sampler they use, and download the data they need.

To run them on your own computer, clone the [repository](https://github.com/AllenDowney/SurveyDataPyMC):

```bash
git clone https://github.com/AllenDowney/SurveyDataPyMC.git
cd SurveyDataPyMC
```

Then install the packages with pip:

```bash
pip install -r requirements.txt jupyter
```

Or create a conda environment with [mamba](https://mamba.readthedocs.io/) (or conda):

```bash
mamba env create -f environment.yml
conda activate SurveyDataPyMC
```

Then run `jupyter lab` and open the notebooks in the `notebooks` folder.

## Next steps

* [Survey Data with Pandas](https://allendowney.github.io/SurveyDataPandas/), the companion tutorial: exploring the same GSS data with pandas and StatsModels.
* [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online.
* The [PyMC documentation](https://www.pymc.io/projects/docs/en/latest/) and [example gallery](https://www.pymc.io/projects/examples/en/latest/).
* [My other workshops](https://allendowney.github.io/#workshops).

The code is available under the [MIT License](https://github.com/AllenDowney/SurveyDataPyMC/blob/main/LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
