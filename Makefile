venv:
	python3 -m venv .venvj

install:
	pip install -r requirements.txt

pylint:
	pylint main.py
