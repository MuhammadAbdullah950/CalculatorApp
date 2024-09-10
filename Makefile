install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C calc.py
test:
	python -m pytest -vv --cov=calc test_calc.py
