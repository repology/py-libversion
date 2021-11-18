PYTEST?=	pytest
FLAKE8?=	flake8
MYPY?=		mypy
ISORT?=		isort
PYTHON?=	python3
TWINE?=		twine

lint: test flake8 mypy isort-check

test::
	${PYTEST} ${PYTEST_ARGS} -v -rs

flake8::
	${FLAKE8} ${FLAKE8_ARGS} --application-import-names=libversion libversion tests

mypy::
	${MYPY} ${MYPY_ARGS} libversion

isort-check::
	${ISORT} ${ISORT_ARGS} --check libversion/*.py tests/*.py

isort::
	${ISORT} ${ISORT_ARGS} libversion/*.py tests/*.py

sdist::
	${PYTHON} setup.py sdist

release::
	rm -rf dist
	${PYTHON} setup.py sdist
	${TWINE} upload dist/*.tar.gz
