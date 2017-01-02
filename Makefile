

test:
	pep8 dict_validator
	pyflakes dict_validator
	./custom_pylint.py --rcfile=dict_validator/.pylintrc dict_validator
	nosetests

docs:
	./build_docs.sh

publish-docs: docs
	./publish_docs.sh

publish: test publish-docs
	python setup.py sdist bdist_wheel upload -r pypi

.PHONY: test publish docs publish-docs
