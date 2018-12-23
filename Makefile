.PHONY: test build init

problem%:
	poetry run python solutions/problem$*.py

test:
	poetry run pytest --doctest-modules

build:
	poetry build

init:
	poetry install
