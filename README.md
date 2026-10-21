# Bayesian Regression for Survey Data with PyMC

[![tests](https://github.com/AllenDowney/SurveyDataPyMC/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/SurveyDataPyMC/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com) and [Alexander Fengler](https://github.com/AlexanderFengler)

In this tutorial, we explore Bayesian regression using PyMC -- the primary library for Bayesian sampling in Python -- focusing on survey data and other datasets with categorical outcomes. Starting with logistic regression, we'll build up to categorical and ordered logistic regression, showcasing how Bayesian approaches provide versatile tools for developing and evaluating complex models. Participants will leave with practical skills for implementing Bayesian regression models in PyMC, along with a deeper appreciation for the power of Bayesian inference in real-world data analysis.

The examples use data from the [General Social Survey](https://gss.norc.org/) (GSS).

The [tutorial site](https://allendowney.github.io/SurveyDataPyMC/) has the notebooks with solutions. This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops). Its companion, [Survey Data with Pandas](https://allendowney.github.io/SurveyDataPandas/), uses the same GSS data.

**Level:** intermediate. You should be comfortable with Python, NumPy and pandas, and basic statistics. You don't need any experience with Bayesian methods or PyMC.

**Length:** about 90 minutes.

## Outline

0. **Introduction to Bayesian sampling:** using PyMC as a random number generator, then building up a model from an uncertain probability, a latent propensity, and observed data.
1. **Logistic regression:** modeling a binary outcome, whether people say other people can be trusted, as a function of time and political party. Priors, the posterior distribution, sampling diagnostics, centering, and generating predictions.
2. **Categorical regression:** extending logistic regression to an unordered outcome with more than two categories, the 2020 presidential vote, as a function of age and gender.
3. **Ordinal regression:** modeling an ordered outcome, how happy people say they are, with cutpoints, as a function of age and birth cohort.

Each notebook comes in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| 0. Introduction to Bayesian sampling | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/00_intro.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/soln/00_intro.ipynb) |
| 1. Logistic regression | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/01_logistic_regression.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/soln/01_logistic_regression.ipynb) |
| 2. Categorical regression | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/02_categorical_regression.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/soln/02_categorical_regression.ipynb) |
| 3. Ordinal regression | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/03_ordinal_regression.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/soln/03_ordinal_regression.ipynb) |

There is also a bonus notebook, still a draft, on a [hierarchical categorical model](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/soln/04_hierarchical.ipynb) of vote by gender identity.

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vSjMfp2TotFMnfpqoefutAEGue3p94qmbSshnnyZH0cs6o33JiGiSH5FxRPQ9qO30G12HDIhQI-vQkH/pub).

### Data

The notebooks download `gss_extract_2022_4.hdf`, an extract of the GSS (2022 release 4) made in the [GssExtract](https://github.com/AllenDowney/GssExtract) repository.

## Recordings

We presented this tutorial at ODSC East 2025 (May 13, 2025). It was not recorded. The version of the code we presented is tagged [`odsc-east-2025`](https://github.com/AllenDowney/SurveyDataPyMC/tree/odsc-east-2025).

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. The notebooks install [nutpie](https://github.com/pymc-devs/nutpie), the sampler they use, and download the data they need.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, pandas, Matplotlib, SciPy, PyTables, PyMC 5, ArviZ (before version 1), nutpie, and Graphviz. You can [download the code in this zip file](https://github.com/AllenDowney/SurveyDataPyMC/archive/main.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/SurveyDataPyMC
cd SurveyDataPyMC
```

Then install the packages with pip:

```
pip install -r requirements.txt jupyter
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate SurveyDataPyMC
```

Then run `jupyter lab` and open the notebooks in the `notebooks` folder.

## Next steps

* [Survey Data with Pandas](https://allendowney.github.io/SurveyDataPandas/), the companion tutorial: exploring the same GSS data with pandas and StatsModels.
* [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online.
* The [PyMC documentation](https://www.pymc.io/projects/docs/en/latest/) and [example gallery](https://www.pymc.io/projects/examples/en/latest/).
* [*Statistical Rethinking*](https://xcelab.net/rm/statistical-rethinking/) by Richard McElreath.
* [My other workshops](https://allendowney.github.io/#workshops).

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
