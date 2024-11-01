.PHONY: test coverage clean

test:
	python3 -m pytest tests/

coverage:
	python3 -m coverage run -m pytest
	python3 -m coverage report -m

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .coverage htmlcov/