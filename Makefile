NAME=$(shell python setup.py --name)
AUTHOR=$(shell python setup.py --author)
VERSION=$(shell python setup.py --version)

test:
	pep8 dict_validator
	pyflakes dict_validator
	./custom_pylint.py --rcfile=dict_validator/.pylintrc dict_validator
	./setup.py nosetests

docs:
	find dict_validator -name '*.py' ! -name '__init__.py' -print0 | \
	    xargs -0 sphinx-apidoc -f -F -d 6 \
	    -H "$(NAME)" \
	    -A "$(AUTHOR)" \
	    -V "$(VERSION)" \
	    -R "$(VERSION)" \
	    dict_validator -o .docs dict_validator
	sed -i "s/alabaster/sphinx_rtd_theme/g" .docs/conf.py
	sphinx-build -b html .docs .docs/html
	@echo "Docs @ file://$(CURDIR)/.docs/html/index.html"

publish: docs
	./publish_docs.sh $(shell git config --get remote.origin.url)
	python setup.py sdist bdist_wheel upload -r pypi

.PHONY: test publish docs
