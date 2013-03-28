import os
import shutil
import wsgi_intercept
from wsgi_intercept import httplib2_intercept

from tiddlyweb.model.bag import Bag
from tiddlyweb.model.tiddler import Tiddler
from tiddlyweb.web.serve import load_app
from tiddlyweb.store import Store
from tiddlywebconfig import config

config['server_host'] = {
    'scheme': 'http',
    'host': 'our_test_domain',
    'port': '8001',
}

config['server_store'] = ['text', { 'store_root': 'store' }]

config['twikified.socket'] = '/tmp/wst.sock'

def _get_store():
    return Store(config['server_store'][0], config['server_store'][1],
                 environ={'tiddlyweb.config': config})


def reset_store():
    if os.path.exists('store'):
        shutil.rmtree('store')


def initialize_app():
    app = load_app()

    def app_fn():
        return app

    httplib2_intercept.install()
    wsgi_intercept.add_wsgi_intercept('our_test_domain', 8001, app_fn)


def create_test_data():
    testbag = Bag(name='testbag')

    WikiTextTiddler = Tiddler('WikiTextTiddler')
    WikiTextTiddler.modifier = 'WikiAuthor'
    WikiTextTiddler.text = u"A ''tiddler'' //with// {{{wikitext}}}"
    WikiTextTiddler.bag = testbag.name

    store = _get_store()
    store.put(testbag)
    store.put(WikiTextTiddler)