test:
	pep8 dict_validator
	pyflakes dict_validator
	pylint --rcfile=dict_validator/.pylintrc dict_validator
	pep8 test
	pyflakes test
	pylint --rcfile=test/.pylintrc test
	./setup.py nosetests

.PHONY: test