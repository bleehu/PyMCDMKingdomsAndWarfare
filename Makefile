init:
	pip install -r requirements-dev.txt
ci:
	pytest test

flake8:
	flake8 --ignore=E501,F401,E128,E402,E731,F821 requests

coverage:
	pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info