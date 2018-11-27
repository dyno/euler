.PHONY: test build init 

test:
	poetry run pytest

build:
	poetry build

init:
	poetry install
