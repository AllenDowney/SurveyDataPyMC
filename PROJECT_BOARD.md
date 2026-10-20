# SurveyDataPyMC Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (2026-10-20)

**Context:** SurveyDataPyMC is a "current" workshop (GreenTeaPress Task 24). The guide is the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple and CompStats are the worked examples. Given at ODSC East 2025 (May 13, 2025), with Alexander Fengler; not recorded. 12 stars; last workshop change 2025-05-13. Companion workshop: SurveyDataPandas (same GSS data and audience, PyCon US 2025); the two should link to each other.

**0. Set up**
- [x] `git fetch`, pulled one commit (README: venues, link to the workshops list); uncommitted edits and untracked files listed (Inventory, below) (2026-10-20)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-20)
- [x] Tags: `odsc-east-2025` at `6008d7a` (2025-05-13 09:34 EDT, the last commit before the tutorial; no recording, but tagged as in SurveyDataPandas), `pre-refresh-2026` at `64bccf8`. Both pushed (2026-10-20)
- [x] Leftovers (Decisions): `gender_id/` moved to `~/GenderId`; cookiecutter scaffolding, `pyproject.toml`, `setup.cfg`, `soln/00_intro.py`, `nlsy-lifetime-outcomes.zip` deleted (backed up to the session scratchpad); `.nc`, `.hdf`, `.vscode/`, `jb/_build/` and the copied `jb` notebooks ignored; `jb/_config.yml`, `soln/build.sh`, `soln/remove_soln.py` committed
- [x] Inventory (below)
- [x] Environment: `mamba env create -f environment.yml` (name `SurveyDataPyMC`, recreated 2026-10-20; Python 3.12.15, PyMC 5.28.5, ArviZ 0.23.4, PyTensor 2.38.3, NumPy 2.4, pandas 3.0, Matplotlib 3.10.9 (pinned, Decisions), SciPy 1.18, PyTables 3.11)

**1. Runs in a current environment**
- [x] `environment.yml` (Python 3.12, conda-forge, Jupyter, the libraries, `matplotlib<3.11`, `pymc>=5.28,<6`, `arviz<1`, python-graphviz, pytest, nbmake, the site build tools) replaces `environment.yaml` (Python 3.11, `defaults`, numpyro/blackjax/optax/nutpie, none used); `requirements.txt` (numpy, pandas, `matplotlib<3.11`, scipy, tables, `pymc>=5.28,<6`, `arviz<1`, graphviz; dev tools dropped); `requirements-dev.txt` (adds jupyter, pytest, nbmake); `Makefile` rewritten as in SurveyDataPandas (`make tests` runs `soln/0*` and `notebooks/0*`) (2026-10-20)
- [x] First code cell (2026-10-20): `%pip install -q nutpie` if it's missing (Colab lacks it), before the `# Get utils.py` cell (Decisions: nutpie). Otherwise Colab has everything (backend-info, 2026-10-20: PyMC 5.28.5, ArviZ 0.22.0, PyTensor 2.38.3, pandas 2.2.3, NumPy 2.1.3, Matplotlib 3.10.0, SciPy 1.16.3, tables 3.10.2, graphviz 0.21). The notebooks already download `utils.py` and the data
- [x] Breakage and warnings (2026-10-20): none in our code. All five solution notebooks run in scratch copies with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors, both in a Colab-matched env (PyMC 5.28.5, ArviZ 0.22, pandas 2.2, Matplotlib 3.10) and in the new env (pandas 3.0, NumPy 2.4). Expected exceptions: the `# Modify this` placeholder in `03` (`p = 0`, "`p` parameters sum to 0"); ArviZ 0.23's import notice about its 1.0 refactor; a `MatplotlibDeprecationWarning` from inside ArviZ 0.x plotting with Matplotlib 3.11 (not on Colab's 3.10). Times (run in parallel): 00 ~0.5 min, 01 ~4.5, 02 ~1, 03 ~6, 04 ~3
- [x] Data URL: `GssExtract/raw/main/data/interim/gss_extract_2022_4.hdf` works (2026-10-20)
- [x] Running instructions: Colab, then pip or mamba, in `jb/index.md` and the README (the README's Makefile/`environment.yaml` section replaced) (2026-10-20)
- [x] Sampling speed (2026-10-20): reviewed the newer versions of these models in `~/pymc-workshop/solutions/Session5_2-Generalized_linear_models.ipynb`. Same models; it uses `draws=250` with the default 1000 tuning steps (no faster) and `var_names` to save only the parameters. Benchmark, 03 age + cohort model (66,958 rows, 4 chains): PyMC NUTS 500+500 ~300 s; 250 draws + tune 1000 284 s; nutpie 500+500 139 s; data collapsed to counts by (age, cohort) (2,413 rows, Multinomial) 10–12 s, same posterior. Adopted: nutpie as the default sampler in `load_idata_or_sample` (and in `00_intro`'s one `pm.sample` call); `var_names=["alpha", "beta"]` for `logistic_model3` (its saved idata went from 47 MB to 0.9 MB). `utils.py` converts nutpie's dict attribute (`idata.attrs["sample_stats"]`) to a string so `az.to_netcdf` can save it. All five solution notebooks pass with warnings as errors; times in parallel: 00 19 s, 01 114 s, 02 74 s, 03 234 s, 04 114 s
- [x] `soln/remove_soln.py` processed only its first argument, so `build.sh` stripped solutions from `00_intro` only (Content issues 3); now it processes every file (2026-10-20). Student versions not regenerated yet (step 3)

**2. Tests and CI**
- [ ] `pytest --nbmake` on the solution and student versions (sampling time matters: check how long each notebook takes)
- [ ] `.github/workflows/tests.yml`; watch the first run
- [ ] Status badge in the README

**3. Colab**
- [ ] Colab cells: the solution version opens itself and links to the version with blanks; `remove_soln.py` rewrites it for the student version; fix `04_hierarchical`'s link (it points to notebook 02)
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos and broken links
- [ ] Layout and license: title cell, Colab cell, copyright and license at the end
- [ ] Content issues (below)

**5. README in the standard shape**
- [ ] README rewritten (fix the `03_ordered_regression` name and the `.iypnb` link); `LICENSE` covers the code (MIT, exists)

**6. Site and visibility**
- [ ] Rebuild the existing site (`jb/`, `gh-pages`), with `prep_notebooks.py` from the template; delete the old `jb/_build/` first
- [ ] Add `04_hierarchical` to `_toc.yml` (bonus; Decisions)
- [ ] SEO checklist
- [ ] Publish; `Sitemap:` line in `~/AllenDowney.github.io/robots.txt`; Search Console; GreenTeaPress Task 22
- [ ] Cross-links with SurveyDataPandas (README and site, both ways); hub entry; repo description and topics

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

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
- `04_hierarchical` is a bonus notebook on the site: add it to the TOC, fix its Colab link, test it in CI.
- `force-run`: not merged (no `force_run=True`); remote branch deleted. The `odsc-east-2025` tag stays at `6008d7a` (the tutorial's start time is unknown).
- `af-review-notebook-3-v2`: tagged `af-review-notebook-3-v2` (pushed), remote branch deleted.
- `~/GenderId` stays a local repo for now (no GitHub repo).
- Target Colab's PyMC 5 / ArviZ 0.x: pin `pymc>=5.28,<6` and `arviz<1` (PyMC 6.3 / ArviZ 1.3 break every notebook: `az.plot_posterior`, `az.to_netcdf` and others are gone). Porting is Content issue 4.
- Sampler: nutpie (the default in current PyMC), set in `utils.py`; `%pip install` cell for Colab. Keep the per-respondent models (collapsing to counts is Content issue 6). Save only the parameters where a model has per-respondent Deterministics (`logistic_model3`).
- CI: quick mode only (fewer draws), every run.
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
3. **The student versions of 01–04 contain the solutions.** `notebooks/01`–`04` have the same cell sources as `soln/` (only `00_intro` had its `# Solution` cells removed), because `remove_soln.py` read only `sys.argv[1]`. This has been live since 2025-05-13 (README and site Colab links). Script fixed; regenerate in step 3.
4. Port to PyMC 6 / ArviZ 1 when Colab moves to them (ArviZ 1.0 reorganized its API; plotting moved to `arviz_plots`).
5. Resolved 2026-10-20 (Decisions: commit executed solutions). The solution notebooks are saved without outputs (except `04_hierarchical`), and the site builds with execution off, so the published pages have no plots, tables or sampler output. Options: commit executed solution notebooks (as in SurveyDataPandas), or have Jupyter Book execute them (slow: about 15 minutes of sampling).
6. Collapsing the data into counts (Binomial by year and party in 01, Multinomial by age and gender in 02, by age and cohort in 03) samples about 25 times faster with the same posterior, but changes the likelihoods and exercises. Not done (Allen, 2026-10-20); maybe for a later revision, or as an aside.
