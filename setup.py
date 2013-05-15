
AUTHOR = 'Chris Dent'
AUTHOR_EMAIL = 'cdent@peermore.com'
MAINTAINER = 'Ben Paddock'
MAINTAINER_EMAIL = 'pads@thisispads.me.uk'
NAME = 'tiddlywebplugins.twikified'
DESCRIPTION = 'Interface between TiddlyWeb and the node.js wikifier for TiddlyWiki text'
VERSION = '0.1.1'

import os
from setuptools import setup, find_packages

setup(
        namespace_packages = ['tiddlywebplugins'],
        name = NAME,
        version = VERSION,
        description = DESCRIPTION,
        long_description = file(os.path.join(os.path.dirname(__file__), 'README')).read(),
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        maintainer = MAINTAINER,
        maintainer_email = MAINTAINER_EMAIL,
        url = 'http://pypi.python.org/pypi/%s' % NAME,
        packages = find_packages(exclude=['test']),
        platforms = 'Posix; MacOS X; Windows',
        install_requires = ['tiddlyweb', 'httplib2', 'wsgi_intercept'],
        zip_safe = False,
)
