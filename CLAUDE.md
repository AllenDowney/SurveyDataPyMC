# SurveyDataPyMC

Allen Downey and Alexander Fengler's tutorial "Survey Data with PyMC": Bayesian regression with PyMC on General Social Survey (GSS) data (logistic, categorical and ordinal regression, plus a bonus hierarchical model). Given at ODSC East 2025 (May 13, 2025); not recorded. The GitHub Pages site (`allendowney.github.io/SurveyDataPyMC/`) is the Jupyter Book in `jb/`, published to the `gh-pages` branch.

Companion workshop: SurveyDataPandas (`~/SurveyDataPandas`; the same GSS data with pandas and StatsModels, same audience). The two link to each other.

**Guide for the 2026 refresh:** the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple and CompStats are the worked examples). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

- `soln/00_intro.ipynb` to `soln/03_ordinal_regression.ipynb`: the solution versions, the ones to edit. `soln/04_hierarchical.ipynb` is a bonus notebook, not on the site.
- `notebooks/`: the versions with blanks, generated from the solution versions by `soln/build.sh` (`remove_soln.py` drops cells that start with `# Solution` and clears outputs). Don't edit them by hand.
- `soln/utils.py` (copied to `notebooks/utils.py`): helpers the notebooks download from GitHub, including `load_idata_or_sample`, which caches sampling results in `.nc` files (ignored).

The notebooks download their data from the GssExtract repo (`https://github.com/AllenDowney/GssExtract/raw/main/data/interim/`).

## Tags

- `odsc-east-2025`: the version given at ODSC East 2025 (not recorded).
- `pre-refresh-2026`: the state before the 2026 refresh.

## Testing

Environment: `mamba env create -f environment.yml` (name `SurveyDataPyMC`). Tests: `pytest --nbmake` on the notebooks (set up in step 2 of the refresh).

The target environment is Google Colab's current Python and libraries.

## Conventions

- Don't change the substance of the text; list content questions under "Content issues" on the board for Allen to decide.
- Keep the student and solution versions in sync by regenerating the student versions from `soln/`.
