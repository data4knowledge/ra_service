import pytest
from model.grid import GRID

def test_ror():
    params = {'identifier': 'xxx'}
    item = GRID(**params)
    assert item.identifier == 'xxx'

