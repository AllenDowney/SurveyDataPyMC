import sys
from os.path import basename
import nbformat as nbf


def remove_soln(filename):
    ntbk = nbf.read(filename, nbf.NO_CONVERT)

    colab_url = ('https://colab.research.google.com/github/AllenDowney/'
                 'SurveyDataPyMC/blob/main/notebooks/' + basename(filename))
    colab_cell = f'[Click here to run this notebook on Colab]({colab_url})'

    keep_cells = []

    for cell in ntbk.cells:
        # skip empty cells
        source = cell['source']
        if len(source) == 0:
            continue

        # skip solutions
        if source.startswith('# Solution'):
            continue

        # point the Colab link at this version
        if source.startswith('[Click here to run this notebook on Colab]'):
            cell['source'] = colab_cell

        # remove the output of code cells
        if cell['cell_type'] == 'code':
            cell['outputs'] = []

        keep_cells.append(cell)

    ntbk.cells = keep_cells

    print('Removing solutions from', filename)
    nbf.write(ntbk, filename)


for filename in sys.argv[1:]:
    remove_soln(filename)
