#
# Makefile for prime-table
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

DEPS ?= $(PWD)/requirements.txt
VENV ?= $(PWD)/venv
MAKE := $(MAKE) --no-print-directory

.PHONY: help venv reset test clean
.DEFAULT_GOAL : help

help:
	@echo 'Usage:'
	@echo
	@echo '    make venv         install the package in a virtual environment'
	@echo '    make reset        recreate the virtual environment'
	@echo '    make test         run the test suite, report coverage'
	@echo '    make clean        cleanup all temporary files'
	@echo '    make clean-pyc    cleanup all python file artifacts'
	@echo '    make clean-venv   cleanup all virtualenv'
	@echo

venv:
	virtualenv $(VENV) --no-site-packages
	. $(VENV)/bin/activate && \
	pip install -r $(DEPS)

reset:
	$(MAKE) clean
	rm -rf "$(VENV)"
	$(MAKE) install

test:
	. $(VENV)/bin/activate && \
	cd code && \
	py.test -vra test

clean: clean-pyc clean-venv

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-venv:
	rm -rf "$(VENV)"
