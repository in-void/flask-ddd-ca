.PHONY: tests


venv:
	virtualenv --python=python3 venv


run:
	. venv/bin/activate; python3 run.py


install: venv
	. venv/bin/activate; pip install .


tests:
	. venv/bin/activate; py.test


clean:
	rm -rf venv


nopyc:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete