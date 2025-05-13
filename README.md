# SurveyDataPyMC

**Abstract**

In this tutorial, we explore Bayesian regression using PyMC -- the primary library for Bayesian sampling in Python -- focusing on survey data and other datasets with categorical outcomes. Starting with logistic regression, we'll build up to categorical and ordered logistic regression, showcasing how Bayesian approaches provide versatile tools for developing and evaluating complex models. Participants will leave with practical skills for implementing Bayesian regression models in PyMC, along with a deeper appreciation for the power of Bayesian inference in real-world data analysis. Participants should be familiar with Python, the SciPy ecosystem, and basic statistics, but no experience with Bayesian methods is required.

**Description**

In this hands-on tutorial, we will dive into the world of Bayesian regression using PyMC, with a particular focus on datasets that feature categorical outcomes. PyMC provides versatile tools for iterative development of powerful models. This tutorial guides participants through the fundamentals of Bayesian regression, starting from logistic regression and extending to categorical and ordered logistic regression. It also introduces the PyMC package, its syntax and capabilities.

Outline:

* Logistic Regression with PyMC

  - Overview of Bayesian inference
  - Modeling binary outcomes with logistic regression
  - Introduction to PyMC and its capabilities
  - Hands-on example: Trust and political alignment

* Categorical Regression

  - Extending logistic regression to multi-class outcomes
  - Differences between Bayesian models and GLM
  - Hands-on example: Age, gender, and voting patterns

* Ordered Logistic Regression
  - Introduction to ordinal outcomes and their challenges
  - Implementing ordered logistic regression in PyMC
  - Hands-on example: Birth cohort and happiness

* Conclusion and Q&A
  - Recap of key concepts
  - Resources for further learning
  - Open discussion and questions

This tutorial is aimed at data scientists who are comfortable with Python, the SciPy ecosystem, and basic statistics but are new to Bayesian statistics and/or PyMC. By the end of the session, participants will have hands-on experience with Bayesian regression models and a solid understanding of how to apply these techniques to real-world data analysis. 

Notes:
The material for the tutorial is in this repository:
https://github.com/AllenDowney/SurveyDataPyMC/tree/main/notebooks

The dataset from the General Social Survey (GSS) can be found here:
https://gssdataexplorer.norc.org/

[The slides for the tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vSjMfp2TotFMnfpqoefutAEGue3p94qmbSshnnyZH0cs6o33JiGiSH5FxRPQ9qO30G12HDIhQI-vQkH/pub).


## Notebooks

The workshop consists of three notebooks that build on each other:

1. `01_logistic_regression.ipynb` 
   - Introduction to PyMC
   - Bayesian logistic regression
   - Analyzing trust and political alignment

2. `02_categorical_regression.ipynb`
   - Multi-class categorical regression
   - Analyzing voting patterns by age and gender

3. `03_ordered_regression.ipynb` 
   - Ordered logistic regression
   - Analyzing happiness by birth cohort

## Setup Instructions

The easiest option is to run the notebooks on Colab, so you don't have to install anything.
Use the following links to open the notebooks:

* [Notebook 1: Logistic Regression](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/01_logistic_regression.ipynb)

* [Notebook 2: Categorical Regression](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/02_categorical_regression.ipynb) 

* [Notebook 3: Ordered Regression](https://colab.research.google.com/github/AllenDowney/SurveyDataPyMC/blob/main/notebooks/03_ordered_regression.ipynb)

**Note:** The notebooks use data from the General Social Survey (GSS).
It will be downloaded automatically when you run the notebooks.

If you want to run the notebooks on your own computer, follow the instructions in the next section.


### Environment Setup

#### Option 1: Using Make (Recommended)
1. Create and activate the conda environment:
```bash
make create_environment
conda activate SurveyDataPyMC
```

2. Install Python dependencies:
```bash
make requirements
```

#### Option 2: Using environment.yaml
Alternatively, you can create the environment directly from the environment.yaml file:
```bash
conda env create -f environment.yaml
conda activate SurveyDataPyMC
```

This will install all required packages including:
- PyMC (≥5.0)
- JupyterLab and Notebook
- Data analysis libraries (numpy, pandas)
- Visualization tools (matplotlib, seaborn)
- Development tools (black, flake8, isort)

### Running the Notebooks

1. Start JupyterLab:
```bash
jupyter lab
```

2. Navigate to the notebooks directory and open the desired notebook.

## Resources

### PyMC Documentation
- [PyMC Documentation](https://www.pymc.io/projects/docs/en/latest/)
- [PyMC Examples](https://www.pymc.io/projects/examples/en/latest/)

### Bayesian Statistics
- [Think Bayes](https://allendowney.github.io/ThinkBayes2/) by Allen Downey
- [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/) by Richard McElreath


