
VERSION := 1.1.0
ARCHIVE := tsk-$(VERSION).zip

.PHONY: all pdb

all:
	python -m pytest ./tests

pdb:
	python -m pytest ./tests --pdb

save: archive/$(ARCHIVE)

archive/$(ARCHIVE):
	git archive -o archive/$(ARCHIVE) HEAD
