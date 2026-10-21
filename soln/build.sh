# copy the notebooks into ../notebooks
cp 0*.ipynb ../notebooks/
cp utils.py ../notebooks/

# run the remove_soln.py script in the ../notebooks directory
python remove_soln.py ../notebooks/0*.ipynb

# push the notebooks to GitHub
cd ../notebooks; git add 0*.ipynb
git commit -m "Update notebooks"
git push origin main

