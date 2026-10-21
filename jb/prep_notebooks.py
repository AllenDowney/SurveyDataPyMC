"""Copy the solution notebooks into jb/ and prepare them for the book.

For each ../soln/NN_name.ipynb, writes NN_name.ipynb here:
- code cells that start with "# Solution" get the hide-cell tag,
  so the solutions are collapsed on the page;
- warnings in stderr outputs are removed (e.g. ArviZ's notice about
  its 1.0 refactor, with a local path in it);
- the page description goes in the notebook metadata (see GreenTeaPress plans/seo.md).

The solution notebooks are committed with their outputs, so the book doesn't run them.
"""

import nbformat

DESCRIPTIONS = {
    '00_intro': "An introduction to Bayesian sampling with PyMC: generate random data, "
                "then build a model with an uncertain probability and a latent propensity.",
    '01_logistic_regression': "Bayesian logistic regression with PyMC: how trust in other people "
                              "has changed over time, by political party, in General Social Survey data.",
    '02_categorical_regression': "Bayesian categorical regression with PyMC: model the 2020 presidential "
                                 "vote by age and gender, using General Social Survey data.",
    '03_ordinal_regression': "Bayesian ordinal regression with PyMC: model how happy people say they are, "
                             "with cutpoints, by age and birth cohort, using General Social Survey data.",
}


def prepare(name, description):
    nb = nbformat.read(f'../soln/{name}.ipynb', 4)

    for cell in nb.cells:
        if cell.cell_type != 'code':
            continue
        if cell.source.startswith('# Solution'):
            tags = cell.metadata.setdefault('tags', [])
            if 'hide-cell' not in tags:
                tags.append('hide-cell')
        cell.outputs = [output for output in cell.outputs
                        if not (output.get('name') == 'stderr' and 'Warning' in output.text)]

    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name} ({len(description)} characters)')


for name, description in DESCRIPTIONS.items():
    prepare(name, description)
