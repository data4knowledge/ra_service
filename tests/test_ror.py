import pytest
from model.ror import ROR

def test_ror():
    params = {'identifier': 'xxx'}
    item = ROR(**params)
    assert item.identifier == 'xxx'

