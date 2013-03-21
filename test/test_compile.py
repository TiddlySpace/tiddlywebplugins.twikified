def test_compile():
	try:
		import tiddlywebplugins.twikified
		assert True
	except ImportError, exc:
		assert False, exc
