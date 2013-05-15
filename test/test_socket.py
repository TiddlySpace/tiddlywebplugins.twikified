"""
Test that twikified can read in tiddlers from a socket mimicking twikifier
"""
import os
import httplib2

from fixtures import initialize_app, reset_store, create_test_data
from fake_twikifier import start_server

socket_file = '/tmp/wst.sock'

expected_twikified_content='<div>A <strong>tiddler</strong> <em>with</em> <code>wikitext</code></div>'
expected_raw_content='<pre class="wikitext">A ''tiddler'' //with// {{{wikitext}}}</pre>'


def setup_function(func):
    initialize_app()
    reset_store()
    create_test_data()


def teardown_function(func):
    try:
        os.unlink(socket_file)
    except OSError:
        pass


def test_get_tiddler_with_twikifier_off():
    start_server(socket_file, expected_raw_content)

    http = httplib2.Http()
    response, content = http.request('http://our_test_domain:8001/bags/testbag/tiddlers/WikiTextTiddler',
                                 method='GET')

    assert response['status'] == '200', content
    assert expected_raw_content in content, 'tiddler should have raw content, is %s' % content


def test_get_tiddler_with_twikifier_on():
    start_server(socket_file, expected_twikified_content)

    http = httplib2.Http()
    response, content = http.request('http://our_test_domain:8001/bags/testbag/tiddlers/WikiTextTiddler',
                                     method='GET')

    assert response['status'] == '200', content
    assert expected_twikified_content in content, 'tiddler should have wikitext content, is %s' % content