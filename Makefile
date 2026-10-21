PROJECT_NAME = SurveyDataPyMC

create_environment:
	mamba env create -f environment.yml
	@echo ">>> environment created. Activate with:\nconda activate $(PROJECT_NAME)"

delete_environment:
	mamba env remove --name $(PROJECT_NAME)

requirements:
	python -m pip install -r requirements-dev.txt

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Run the solution notebooks. The versions with blanks don't run top to
# bottom (the blanks break the models), so check_student checks instead
# that they are up to date with the solutions.
tests: check_student
	pytest --nbmake soln/0*.ipynb

# Regenerate the versions with blanks and compare them with notebooks/
check_student:
	@tmp=$$(mktemp -d); \
	cp soln/0*.ipynb $$tmp/; \
	python soln/remove_soln.py $$tmp/0*.ipynb > /dev/null; \
	status=0; \
	for f in $$tmp/0*.ipynb; do \
		cmp -s $$f notebooks/$$(basename $$f) || { echo "notebooks/$$(basename $$f) is out of date; run soln/build.sh"; status=1; }; \
	done; \
	cmp -s soln/utils.py notebooks/utils.py || { echo "notebooks/utils.py differs from soln/utils.py"; status=1; }; \
	rm -rf $$tmp; exit $$status
