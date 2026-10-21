# SurveyDataPyMC Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** DONE (2026-10-21). Still open: Allen submits the sitemap in Search Console; the 04 rewrite and content issues 9–14 (below)

**Context:** SurveyDataPyMC is a "current" workshop (GreenTeaPress Task 24). The guide is the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are the worked examples. Given at ODSC East 2025 (May 13, 2025), with Alexander Fengler; not recorded. 12 stars; last workshop change 2025-05-13. Companion workshop: SurveyDataPandas (same GSS data and audience, PyCon US 2025); the two should link to each other.

**0. Set up**
- [x] `git fetch`, pulled one commit (README: venues, link to the workshops list); uncommitted edits and untracked files listed (Inventory, below) (2026-10-20)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags: `odsc-east-2025` at `6008d7a` (2025-05-13 09:34 EDT, the last commit before the tutorial; no recording, but tagged as in SurveyDataPandas), `pre-refresh-2026` at `64bccf8`. Both pushed (2026-10-20)
- [x] Leftovers (Decisions): `gender_id/` moved to `~/GenderId`; cookiecutter scaffolding, `pyproject.toml`, `setup.cfg`, `soln/00_intro.py`, `nlsy-lifetime-outcomes.zip` deleted (backed up to the session scratchpad); `.nc`, `.hdf`, `.vscode/`, `jb/_build/` and the copied `jb` notebooks ignored; `jb/_config.yml`, `soln/build.sh`, `soln/remove_soln.py` committed
- [x] Inventory (below)
- [x] Environment: `mamba env create -f environment.yml` (name `SurveyDataPyMC`, recreated 2026-10-20; Python 3.12.15, PyMC 5.28.5, ArviZ 0.23.4, PyTensor 2.38.3, NumPy 2.4, pandas 3.0, Matplotlib 3.10.9 (pinned, Decisions), SciPy 1.18, PyTables 3.11)

**1. Runs in a current environment**
- [x] `environment.yml` (Python 3.13 since 2026-10-21, was 3.12; conda-forge, Jupyter, the libraries, `matplotlib<3.11`, `pymc>=5.28,<6`, `arviz<1`, python-graphviz, pytest, nbmake, the site build tools) replaces `environment.yaml` (Python 3.11, `defaults`, numpyro/blackjax/optax/nutpie, none used); `requirements.txt` (numpy, pandas, `matplotlib<3.11`, scipy, tables, `pymc>=5.28,<6`, `arviz<1`, graphviz; dev tools dropped); `requirements-dev.txt` (adds jupyter, pytest, nbmake); `Makefile` rewritten as in SurveyDataPandas (`make tests` runs `soln/0*` and `notebooks/0*`) (2026-10-20)
- [x] First code cell (2026-10-20): `%pip install -q nutpie` if it's missing (Colab lacks it), before the `# Get utils.py` cell (Decisions: nutpie). Otherwise Colab has everything (backend-info, 2026-10-20: PyMC 5.28.5, ArviZ 0.22.0, PyTensor 2.38.3, pandas 2.2.3, NumPy 2.1.3, Matplotlib 3.10.0, SciPy 1.16.3, tables 3.10.2, graphviz 0.21). The notebooks already download `utils.py` and the data
- [x] Breakage and warnings (2026-10-20): none in our code. All five solution notebooks run in scratch copies with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors, both in a Colab-matched env (PyMC 5.28.5, ArviZ 0.22, pandas 2.2, Matplotlib 3.10) and in the new env (pandas 3.0, NumPy 2.4). Expected exceptions: the `# Modify this` placeholder in `03` (`p = 0`, "`p` parameters sum to 0"); ArviZ 0.23's import notice about its 1.0 refactor; a `MatplotlibDeprecationWarning` from inside ArviZ 0.x plotting with Matplotlib 3.11 (not on Colab's 3.10). Times (run in parallel): 00 ~0.5 min, 01 ~4.5, 02 ~1, 03 ~6, 04 ~3
- [x] Data URL: `GssExtract/raw/main/data/interim/gss_extract_2022_4.hdf` works (2026-10-20)
- [x] Running instructions: Colab, then pip or mamba, in `jb/index.md` and the README (the README's Makefile/`environment.yaml` section replaced) (2026-10-20)
- [x] Sampling speed (2026-10-20): reviewed the newer versions of these models in `~/pymc-workshop/solutions/Session5_2-Generalized_linear_models.ipynb`. Same models; it uses `draws=250` with the default 1000 tuning steps (no faster) and `var_names` to save only the parameters. Benchmark, 03 age + cohort model (66,958 rows, 4 chains): PyMC NUTS 500+500 ~300 s; 250 draws + tune 1000 284 s; nutpie 500+500 139 s; data collapsed to counts by (age, cohort) (2,413 rows, Multinomial) 10–12 s, same posterior. Adopted: nutpie as the default sampler in `load_idata_or_sample` (and in `00_intro`'s one `pm.sample` call); `var_names=["alpha", "beta"]` for `logistic_model3` (its saved idata went from 47 MB to 0.9 MB). `utils.py` converts nutpie's dict attribute (`idata.attrs["sample_stats"]`) to a string so `az.to_netcdf` can save it. All five solution notebooks pass with warnings as errors; times in parallel: 00 19 s, 01 114 s, 02 74 s, 03 234 s, 04 114 s
- [x] `soln/remove_soln.py` processed only its first argument, so `build.sh` stripped solutions from `00_intro` only (Content issues 3); now it processes every file (2026-10-20). Student versions not regenerated yet (step 3)

**2. Tests and CI**
- [x] Quick mode for tests (Decisions) (2026-10-20)
- [x] `make tests` (2026-10-20): `check_student` regenerates the versions with blanks in a temp folder and compares them with `notebooks/` (and `utils.py`), then `pytest --nbmake soln/0*.ipynb`. The versions with blanks don't run top to bottom: each blank breaks its model (`p = 0`), and the cells that use the model's results fail after it (45 error cells in 00–03), so they are checked for sync instead of run. Quick mode: 5 passed in 83 s. Quick mode doesn't load or save the `.nc` caches (stale 2025 caches in `soln/` and `notebooks/` had been loaded instead of sampling; deleted)
- [x] `.github/workflows/tests.yml` (push to main, PR, monthly, manual; Python 3.13 (was 3.12 until 2026-10-21); apt graphviz; pip with `requirements-dev.txt`; `SURVEYDATAPYMC_QUICK=1`; 30-minute timeout; checkout@v5, setup-python@v6) (2026-10-20)
- [x] First run passed (2026-10-20, run 39518865071, 4 min 54 s with setup; pushed `53ef06e`..`bfe235c`)
- [x] Status badge in the README

**3. Colab**
- [x] Colab cells (2026-10-20): the solution version opens itself and links to the version with blanks; `remove_soln.py` points it at the student version (this fixes `04_hierarchical`'s link to notebook 02). Student versions regenerated: no `# Solution` cells, no outputs (Content issue 3 fixed)
- [x] Allen ran `soln/01_logistic_regression` on Colab end to end (2026-10-21). First try (2026-10-21): `import pymc` failed (`cannot import name 'concat' from 'arviz'`) because nutpie 0.16.11 requires `arviz>=0.23` and Colab has 0.22, so `pip install nutpie` upgraded ArviZ to 1.x. Fixed: the install cell pins `"arviz<1"` (gets 0.23.4, the version in the env and CI). Second try: the version with blanks fails at the first exercise (`p = 0`, "All initialization points failed"), as expected; 01 now says so before that exercise (Allen). Colab is on Python 3.13 (since 2026-08-19, backend-info), not 3.12: `environment.yml` and CI moved to 3.13 (local env not rebuilt, Allen); checklist in `workshops.md` updated

**4. Text**
- [x] Typos (2026-10-20): codespell ("coefficents") plus a read of all markdown, comments and docstrings. Fixed in 01: "ArViz" → "ArviZ", xarray "`DataSet`" → "`Dataset`", "Pandas" → "pandas", "Well use" → "We'll use", "`draw` indicates" → "`draws`", "`years`" → "`year`" (twice), "age effect" → "year effect" (that model has no age). 02 and 04: "table show", "each responses", stray "]" closing the GSS quotation; 02: "result look like", "third-party candidate"; 03: double space, comment "Compute cumulative logits" → "probabilities" on the `expit` lines; 04: shape comment `(n_obs, 2)` → `(2, n_obs)`; `utils.py` docstrings "Pandas" → "pandas". Not changed: `\( x \)` in 02/04 (valid MathJax)
- [x] Links (2026-10-20): ArviZ `InferenceData` page (404 under `stable`, which is ArviZ 1 now) → `v0.22.0`; Matplotlib `api/axes_api.html` → `stable/api/axes_api.html` (`utils.py`); README `04_hierarchical.iypnb` → `.ipynb`. GSS Data Explorer links dead (Content issues)
- [x] Layout and license (Decisions, 2026-10-20): title cell H1 + "Part of a tutorial on Bayesian regression for survey data with PyMC." (04 had no subtitle); last cell "Copyright 2025–2026 Allen B. Downey and Alexander Fengler", code MIT, text CC BY-NC-SA 4.0; trailing empty code cells removed. Headings were already ATX, one H1, sections `##`. Student versions regenerated; tests pass
- [x] Content issues, first round (Allen, 2026-10-20; below): `round_into_bins` fixed; GSS Data Explorer links replaced; obvious fixes applied
- [ ] Content issues still open (below)

**5. README in the standard shape**
- [x] README rewritten in the standard shape (2026-10-20): title "Bayesian Regression for Survey Data with PyMC" (as SurveyDataPandas calls it); badge; both authors; abstract; level intermediate; length about 90 minutes (Allen); outline 00–03; notebook table with Colab links (exercises and solutions); 04 as a draft bonus; slides; data; recordings (ODSC East 2025, not recorded, tag `odsc-east-2025`); running instructions (Colab, pip, mamba); next steps (SurveyDataPandas, Think Bayes, PyMC docs, Statistical Rethinking, the hub); license. All links checked (200)
- [x] `LICENSE` (MIT): "Copyright (c) 2024–2026 Allen B. Downey and Alexander Fengler" (Allen)

**6. Site and visibility**
- [x] Solution notebooks executed at full size and committed with outputs (2026-10-21; about 5.5 minutes in all with nutpie; timing metadata stripped). `remove_soln.py` now also clears execution counts, cell timing, and saved widget state, so the versions with blanks only change when the content does
- [x] `jb/` from the SurveyDataPandas pattern (2026-10-21): `_config.yml` (execution off, since the notebooks have outputs; sitemap, Open Graph, Think Bayes cover, page-view counter, MathJax path kept); `_toc.yml` 00–03; `build.sh [publish]`; `prep_notebooks.py` (copies `../soln`, hides `# Solution` cells, removes warnings from stderr outputs, writes descriptions); `index.md` rewritten (front matter, H1 "Bayesian Regression for Survey Data with PyMC", authors, level, length, notebooks with Colab links to the versions with blanks, slides, running instructions, next steps, license)
- [x] Test build in a scratch copy (2026-10-21): sitemap lists only the 5 TOC pages; every page has one `name="description"`, one `og:description`, `rel="canonical"`, `og:image`, the counter; titles "Logistic Regression — Survey Data with PyMC" etc. No ArviZ notice or local paths on the pages
- [x] Allen approved the descriptions (2026-10-21)
- [x] `np.set_printoptions(legacy='1.25')` in the import cells (checklist item from SurveyDataPandas); solution notebooks re-run (2026-10-21)
- [x] Published (2026-10-21): old `jb/_build/` deleted (it had the stale `04_hierarchical` page), `./build.sh publish`; `build.sh` files made executable
- [x] `04_hierarchical` off the site: not in `_toc.yml`, and the stale page is gone (404, 2026-10-21) (Decisions)
- [x] `Sitemap:` line in `~/AllenDowney.github.io/robots.txt` (pushed, `cf1763c`) (2026-10-21)
- [ ] Allen submits the sitemap in Search Console (`https://allendowney.github.io/SurveyDataPyMC/sitemap.xml`)
- [x] GreenTeaPress Task 22 line updated (2026-10-21)
- [x] Cross-links with SurveyDataPandas: this README and site link to it; its README and site link here (2026-10-21)
- [x] Hub entry: already right (title, ODSC East 2025)
- [x] Repo description "Bayesian Regression for Survey Data with PyMC: a tutorial on logistic, categorical, and ordinal regression with General Social Survey data"; topic `jupyter-book` added; both also in GreenTeaPress `scripts/repo_about.sh` (uncommitted there) (2026-10-21)

**7. Close**
- [x] Tag `2026-refresh` at `11db69b`, pushed; summary in GreenTeaPress Task 24 (uncommitted there) (2026-10-21)

### Inventory (2026-10-20)

**The workshop:** four notebooks plus a bonus, in two versions. Solutions in `soln/` (executed), versions with blanks in `notebooks/`.

| Notebook | Topic |
|---|---|
| `00_intro` | Introduction to Bayesian sampling |
| `01_logistic_regression` | Logistic regression; trust and political alignment |
| `02_categorical_regression` | Categorical regression; age, gender and voting |
| `03_ordinal_regression` | Ordinal regression; birth cohort and happiness |
| `04_hierarchical` (bonus) | Hierarchical categorical regression; not in the site's TOC; Colab cell points to `02` |

- Each notebook has a Colab cell after the title and a first code cell that downloads `utils.py` from `SurveyDataPyMC/raw/main/notebooks/`. No `%pip` cell. Data from `GssExtract/raw/main/data/interim/`.
- `soln/utils.py` and `notebooks/utils.py` are identical. `load_idata_or_sample` caches sampling results in `.nc` files (about 185 MB of them locally, now ignored).
- The student versions are generated by `soln/build.sh` (copies to `notebooks/`, runs `remove_soln.py`, commits and pushes). `build.sh` and `remove_soln.py` were untracked until now.
- `02`, `03`, `04` start with `%load_ext autoreload`.
- Setup files: `environment.yaml` (Python 3.11, `defaults` channel, PyMC ≥ 5, nutpie, numpyro, blackjax, optax, black, flake8), `requirements.txt` (unpinned, including dev tools), cookiecutter `Makefile`. `LICENSE` exists.

**Site:** `allendowney.github.io/SurveyDataPyMC/`, Pages source `gh-pages` (last published 2025-05-13). `jb/` was half tracked (`_toc.yml`, `index.md`, `build.sh`, `prep_notebooks.py`; `_config.yml` untracked). `build.sh` copies `../soln/0*.ipynb`, runs `prep_notebooks.py` (adds `hide-cell` to solution cells), `jb build`, then always `ghp-import -n -p -f`. Execution is off. `04_hierarchical.html` is published though it isn't in the TOC (stale `_build`).

**Remote branches:** `force-run` (1 commit ahead of main: Alexander, 2025-05-13 10:20 EDT, adds `force_run=True` to every `load_idata_or_sample` call and renames one kernel to `odsc_2025`) and `af-review-notebook-3-v2` (2 ahead, 2025-04-27: Alexander's review of notebook 3, superseded by the rewrite in main; only 1 of the 35 cells it changed is in main). The others are merged.

**Local state that was not in git (2026-10-20):**

- `gender_id/`: an ANES 2024 / SOGI research project (3 tracked `.md` files, an uncommitted Phase 2.5 edit to `plan.md`, and about 85 MB of untracked ANES data, scripts, CSVs and an inventory notebook).
- Cookiecutter scaffolding: `data/`, `docs/`, `models/`, `references/`, `reports/`, `surveydatapymc/`, `setup.cfg` (empty or `.gitkeep` only); tracked `pyproject.toml`.
- `soln/00_intro.py` (nbconvert export), `soln/gss_extract_2022_4.hdf` (downloaded data), `nlsy-lifetime-outcomes.zip` (not used by any notebook), `.vscode/`, `notebooks/.gitkeep`.
- `soln/01_logistic_regression.ipynb`: kernel name and Python version changed in the metadata only (discarded; backed up).

### Decisions

Allen, 2026-10-20:

- This thread refreshes SurveyDataPyMC (venue ODSC East 2025, not recorded); SurveyDataPandas is its companion.
- `gender_id/` moves to its own repo: `~/GenderId` (local git repo, initial commit with the uncommitted `plan.md` edit; the ANES `.dta`, `.zip`, `.xlsx` and `.pdf` files are ignored there). Removed from main here; still in history and in `pre-refresh-2026`.
- Tag the ODSC version `odsc-east-2025` at `6008d7a` and `pre-refresh-2026`; push both.
- `04_hierarchical`: bonus notebook in the repo, tested in CI, Colab link fixed; **not on the site** until it's finished (Allen, 2026-10-20, changed from "on the site"; Content issue 10).
- `force-run`: not merged (no `force_run=True`); remote branch deleted. The `odsc-east-2025` tag stays at `6008d7a` (the tutorial's start time is unknown).
- `af-review-notebook-3-v2`: tagged `af-review-notebook-3-v2` (pushed), remote branch deleted.
- `~/GenderId` stays a local repo for now (no GitHub repo).
- README: level intermediate, length about 90 minutes; push after step 5 (2026-10-20).
- Subtitle "Part of a tutorial on Bayesian regression for survey data with PyMC." (matches the site); copyright "2025–2026 Allen B. Downey and Alexander Fengler"; text license CC BY-NC-SA 4.0 (2026-10-20).
- Target Colab's PyMC 5 / ArviZ 0.x: pin `pymc>=5.28,<6` and `arviz<1` (PyMC 6.3 / ArviZ 1.3 break every notebook: `az.plot_posterior`, `az.to_netcdf` and others are gone). Porting is Content issue 4.
- Sampler: nutpie (the default in current PyMC), set in `utils.py`; `%pip install` cell for Colab. Keep the per-respondent models (collapsing to counts is Content issue 6). Save only the parameters where a model has per-respondent Deterministics (`logistic_model3`).
- CI: pip with `requirements-dev.txt` (checklist default); quick mode only, every run. `SURVEYDATAPYMC_QUICK` set: `subsample(data)` (a visible line after each `data = gss.dropna(...)` in 01–04) keeps 5,000 random rows (seed 17), and `load_idata_or_sample` uses `draws=100, tune=100`. Solutions in quick mode, one after another, with warnings as errors: 115 s in all (2026-10-20).
- Student versions regenerated in step 3, with the Colab-cell rewrite (not pushed sooner).
- Site outputs: commit the solution notebooks executed (as in SurveyDataPandas); the site keeps execution off.
- Pin `matplotlib<3.11` (Colab has 3.10): with 3.11, ArviZ 0.x plots emit a `MatplotlibDeprecationWarning`. Remove the pin with the ArviZ 1 port (Content issue 4).
- The notebooks already have cell ids (an nbformat warning in the scratch runs came from the test cell, not the notebooks).
- Cross-links to SurveyDataPandas: site `https://allendowney.github.io/SurveyDataPandas/`, hub `https://allendowney.github.io/#workshops` (SurveyDataPandas refresh done, 2026-10-20).
- Delete the leftovers listed above (backed up to the session scratchpad); ignore caches, data and the `jb` build; commit `jb/_config.yml`. Keep the `Makefile`, updated for `environment.yml` (as in SurveyDataPandas).

### Content issues

(For Allen to decide.)

1. Resolved 2026-10-20 (Decisions): `04_hierarchical` is a bonus on the site.
2. Resolved 2026-10-20 (Decisions): the unmerged branches.
3. Fixed 2026-10-20 (student versions regenerated). **The student versions of 01–04 contained the solutions.** `notebooks/01`–`04` have the same cell sources as `soln/` (only `00_intro` had its `# Solution` cells removed), because `remove_soln.py` read only `sys.argv[1]`. This has been live since 2025-05-13 (README and site Colab links). Script fixed; regenerate in step 3.
4. Port to PyMC 6 / ArviZ 1 when Colab moves to them (ArviZ 1.0 reorganized its API; plotting moved to `arviz_plots`).
5. Resolved 2026-10-20 (Decisions: commit executed solutions). The solution notebooks are saved without outputs (except `04_hierarchical`), and the site builds with execution off, so the published pages have no plots, tables or sampler output. Options: commit executed solution notebooks (as in SurveyDataPandas), or have Jupyter Book execute them (slow: about 15 minutes of sampling).
6. Collapsing the data into counts (Binomial by year and party in 01, Multinomial by age and gender in 02, by age and cohort in 03) samples about 25 times faster with the same posterior, but changes the likelihoods and exercises. Not done (Allen, 2026-10-20); maybe for a later revision, or as an aside.
7. Fixed 2026-10-20: NaN stays NaN (754 respondents with no age were an extra top age group; the bins are now floats). **`round_into_bins` put missing values in a spurious top bin.** `np.digitize` returns `len(bins)` for NaN, so a missing age becomes one bin past the maximum (e.g. `[20, 47, nan, 89]` → `[18, 43, 93, 88]`), and those respondents show up as an extra age group in the crosstabs in 02, 03 and 04 (`age_group`, `birth_group`). Fix: return NaN for NaN input.
8. Fixed 2026-10-20: each "## Data" cell links "General Social Survey" to `https://gss.norc.org/`; the per-variable links are plain text; the README links the homepage. GSS Data Explorer links were dead (`gssdataexplorer.norc.org`: the "Data" sections of 01, 02, 03, 04 link variables 141, 434, 441, 7759; also the README). Same as SurveyDataPandas; drop them or link the GSS codebook.
9. Duplicate headings: "## Categorical Regression" twice in 02 and 04 (and the notebook title is the same), "## Ordinal Regression" twice in 03.
10. Open (off the site until revised). 04_hierarchical looks unfinished: cells copied from 02 (age-group plots, expit/softmax) that no model uses; "interaction between age and gender" and "limit the analysis to people who identify as male or female" contradict the models (five gender groups, no age); "Here's the model with gender as an additional categorical predictor" describes the hierarchical model; `!rm hierarchical_idata.nc` (debugging leftover, fails if the file is missing); no interpretation or conclusion; the prior `mu_alpha ~ Normal(2, 0.3)` is unexplained.
11. Fixed 2026-10-20 except "called sigma" (σ may be deliberate): `sigma_prior` → "the standard deviations of the priors"; "mutable Data" → "Data"; "Compute and save" → "Compute" where nothing is saved; the unfinished and wrong comments in the prediction loop; `pm.plot_pair`/`pm.summary` → `az.`. Was: 01: "try increasing or decreasing `sigma_prior`" (no such variable); "the prior predictive, which we'll talk about later" (never followed up); "Compute and save the probabilities" where `p` isn't saved; "mutable Data" (all `pm.Data` is mutable now); cell with an unfinished comment ("Assign covariates to compute the posterior distributions of") and "Compute the posterior predictive" on `compute_deterministics`; `pm.plot_pair`/`pm.summary` where the rest uses `az.`; "The inverse logit function is called sigma" next to `pm.math.sigmoid`.
12. Partly fixed 2026-10-20: the "Modify this" stub now names `categorical_model2` (the following cells use it, so the student version failed). Open: 02: "estimate the crossover point" is never done; "what the interaction looks like between age and gender" but the model is additive; the "Modify this" stub names the model `categorical_model` but the solution uses `categorical_model2`; `hdi_low`/`hdi_high` hold the 5th and 95th percentiles, not an HDI (also 03).
13. Partly fixed 2026-10-20: comment on the linear predictor. Open: 03: cutpoints written c₁, c₂ in the text but `cutpoint_0`, `cutpoint_1` in the code; "marginal probabilities" for per-category probabilities; "The transform sorts the cutpoints" (it constrains them); comment "Compute cumulative logits" on the linear predictor; text shows `ordinal_model`'s graph and says "let's run the sampler" but samples `ordinal_model_diy`; "about two times bigger" (check against current output); "a little bit of extrapolation" for cohorts 1905–2019 at age 40 (survey years 1945–2059); the `# data = data.sample(5000)` debugging advice is now redundant with `subsample`; one plot without labels.
14. 00: `pm.Normal("p", 0.5, 0.1)` used as a probability (not bounded); the solution changes a prior's sigma from 1 to 3 without saying why.
15. Fixed 2026-10-20 (removed from 02, 03, 04). `%load_ext autoreload` / `%autoreload 2` at the top of 02, 03, 04 (development leftovers; not in 00 or 01).

