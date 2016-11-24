#
# Makefile for prime-table
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

DEPS ?= $(PWD)/requirements.txt
VENV ?= $(PWD)/venv
MAKE := $(MAKE) --no-print-directory

.PHONY: help venv reset test run run-debug clean clean-pyc clean-venv
.DEFAULT_GOAL : help

help:
	@echo 'Usage:'
	@echo
	@echo '    make venv         install the package in a virtual environment'
	@echo '    make reset        recreate the virtual environment'
	@echo '    make test         run the test suite, report coverage'
	@echo '    make run          run main.py'
	@echo '    make run-debug    run main.py in debug mode'
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
	$(MAKE) venv

test:
	. $(VENV)/bin/activate && \
	cd code && \
	py.test -vra test

run:
	. $(VENV)/bin/activate && \
	cd code && \
	python main.py

run-debug:
	. $(VENV)/bin/activate && \
        cd code && \
        python main.py -d

clean:  clean-pyc clean-venv

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '.cache' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-venv:
	rm -rf "$(VENV)"
