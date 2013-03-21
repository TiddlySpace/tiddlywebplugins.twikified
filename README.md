# About

Provides an interface between TiddlyWeb and the node.js wikifier for TiddlyWiki text.
When a request is made to render a tiddler with TiddlyWiki text it is passed on to a node.js module for processing.
It then returns the result back to the client that requested it.

# Requirements

* [Python](http://www.python.org/)
* make
* A working TiddlyWeb instance to test against
* [py.test](http://pytest.org/latest/) to run the tests.

# Contributing

`setup.py` is used to package up the plugin and install it.

Plugin code lives in the `tiddlywebplugins` directory.

Tests live in the `test` directory.

# Usage

`make test` runs the tests.  Currently there is just the one that 
ensures the plugin can be imported.

`make install` installs the plugin as a package on your system 
(you may need sudo for this.)

To set this plugin as the default renderer for all tiddlers, add the following to `tiddlywebconfig.py`:

```
'wikitext.default_renderer': 'tiddlywebplugins.twikified'
```

# See Also

See the accompanying [node module](https://github.com/cdent/twikifier)