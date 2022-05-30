import pytest
from model.dun import DUN

def test_dun_valid():
    params = {'identifier': '123456789'}
    item = DUN(**params)
    assert item.identifier == '123456789'

def test_dun_invalid():
    params = {'identifier': '12345678'}
    with pytest.raises(ValueError):
      item = DUN(**params)


