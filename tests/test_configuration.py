import pytest
from model.configuration import Configuration

def test_configuration_valid():
    params = {'base_uri': 'http://www.d4k.dk', 'server_url': "http://www.d4k.dk"}
    item = Configuration(**params)
    assert item.base_uri == 'http://www.d4k.dk'
    assert item.server_url == 'http://www.d4k.dk'

def test_configuration_invalid_1():
    params = {'base_uri': 'http://www', 'server_url': "http://www.d4k.dk"}
    with pytest.raises(ValueError):
      item = Configuration(**params)

def test_configuration_invalid_2():
    params = {'base_uri': 'http://www.d4k.dk', 'server_url': "//www"}
    with pytest.raises(ValueError):
      item = Configuration(**params)

