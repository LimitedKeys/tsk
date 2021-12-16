
.PHONY: all pdb

all:
	python -m pytest ./tests

pdb:
	python -m pytest ./tests --pdb
