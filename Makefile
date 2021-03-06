ENV=./env/bin
SHELL := /bin/bash
PYTHON=$(ENV)/python
PIP=$(ENV)/pip
MANAGE=$(PYTHON) manage.py

collect_static:
	$(MANAGE) collectstatic --noinput --clear --link

flake8:
	$(ENV)/flake8

migrate:
	$(MANAGE) migrate
	
dev_pip:
	$(PIP) install -r requirements.pip --upgrade	
	
dev:
	$(PIP) install -r requirements/development.txt --upgrade

prod:
	$(PIP) install -r requirements/production.txt --upgrade

env:
	virtualenv -p `which python3` env

clean:
		pyclean .
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf *.egg-info

test:
	$(MANAGE) test

run:
	$(MANAGE) runserver & pytest

freeze:
	mkdir -p requirements
	$(PIP) freeze > requirements/base.txt


# General
REPO=nuxis/p0sX-server

sign:
	drone sign $(REPO)
