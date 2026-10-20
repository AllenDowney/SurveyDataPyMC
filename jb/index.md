# SurveyDataPyMC

**Abstract**

In this tutorial, we explore Bayesian regression using PyMC -- the primary library for Bayesian sampling in Python -- focusing on survey data and other datasets with categorical outcomes. Starting with logistic regression, we'll build up to categorical and ordered logistic regression, showcasing how Bayesian approaches provide versatile tools for developing and evaluating complex models. Participants will leave with practical skills for implementing Bayesian regression models in PyMC, along with a deeper appreciation for the power of Bayesian inference in real-world data analysis. Participants should be familiar with Python, the SciPy ecosystem, and basic statistics, but no experience with Bayesian methods is required.

**Description**

In this hands-on tutorial, we will dive into the world of Bayesian regression using PyMC, with a particular focus on datasets that feature categorical outcomes. PyMC provides versatile tools for iterative development of powerful models. This tutorial guides participants through the fundamentals of Bayesian regression, starting from logistic regression and extending to categorical and ordered logistic regression. It also introduces the PyMC package, its syntax and capabilities.

## Run the notebooks

Use these links to run the notebooks on Colab:

* [Notebook 0: Introduction to Bayesian Sampling](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/00_intro.ipynb)

* [Notebook 1: Logistic Regression](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/01_logistic_regression.ipynb)

* [Notebook 2: Categorical Regression](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/02_categorical_regression.ipynb)

* [Notebook 3: Ordinal Regression](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/03_ordinal_regression.ipynb)

**Note:** The notebooks use data from the General Social Survey (GSS).
The notebooks will download the data when needed.


## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. The notebooks download the data they need.

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
