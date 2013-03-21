# Simple Makefile for some common tasks.
.PHONY: test dist upload

clean:
	find . -name "*.pyc" |xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *.egg-info || true
	rm -r store || true
	rm tiddlyweb.log || true

test:
	py.test -x test

install:
	python setup.py install

dist:
	python setup.py sdist

release: clean pypi

pypi:
	python setup.py sdist upload
