test:
	pep8 dict_validator
	pyflakes dict_validator
	pylint --rcfile=dict_validator/.pylintrc dict_validator
	pep8 test
	pyflakes test
	pylint --rcfile=test/.pylintrc test
	./setup.py nosetests

publish:
	python setup.py sdist bdist_wheel upload -r pypitest

publish-release:
	python setup.py sdist bdist_wheel upload -r pypi

.PHONY: test publish, publish-release