#!/bin/bash

# Exit on error
set -e


# Build the JupyterBook version

# copy notebooks
echo "Copying notebooks..."
cp ../soln/0*.ipynb .
cp ../soln/utils.py .

# add tags to hide the solutions
echo "Processing notebooks..."
python prep_notebooks.py

# build the HTML version
echo "Building JupyterBook..."
jb build .

# push it to GitHub
echo "Pushing to GitHub..."
ghp-import -n -p -f _build/html

echo "Build complete!"
