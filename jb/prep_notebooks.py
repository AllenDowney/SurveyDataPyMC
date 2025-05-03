"""
This script prepares notebooks for JupyterBook by adding appropriate tags to hide solution cells.
It processes all notebooks in the current directory that start with 01, 02, 03, or 04.
"""

import nbformat as nbf
from glob import glob


def process_cell(cell):
    """
    Process a single notebook cell, adding 'hide-cell' tag to solution cells.
    
    Args:
        cell: A notebook cell dictionary containing cell metadata and content
    
    Returns:
        None (modifies cell in place)
    """
    # Get existing tags from cell metadata, or empty list if none exist
    cell_tags = cell.get('metadata', {}).get('tags', [])

    # If this is a code cell that starts with '# Solution',
    # add the 'hide-cell' tag to hide it in the JupyterBook
    if cell['cell_type'] == 'code':
        source = cell['source']
        if source.startswith('# Solution'):
            tag = 'hide-cell'
            if tag not in cell_tags:
                cell_tags.append('hide-cell')

    # Update the cell's metadata with the new tags
    if len(cell_tags) > 0:
        cell['metadata']['tags'] = cell_tags


def process_notebook(path):
    """
    Process an entire notebook file, adding tags to all cells.
    
    Args:
        path: Path to the notebook file
    
    Returns:
        None (modifies notebook file in place)
    """
    # Read the notebook
    ntbk = nbf.read(path, nbf.NO_CONVERT)

    # Process each cell in the notebook
    for cell in ntbk.cells:
        process_cell(cell)

    # Write the modified notebook back to the same file
    nbf.write(ntbk, path)


# Find all notebooks that start with 01, 02, 03, or 04
paths = glob("0[1234]*.ipynb")

# Process each notebook in order
for path in sorted(paths):
    print('Preparing notebook:', path)
    process_notebook(path)
