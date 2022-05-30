import pytest
from model.namespace import Namespace

def test_namespace():
    params = {'name': 'Jack', 'authority': 'xxx'}
    ns = Namespace(**params)
    assert ns.name == "Jack"
    assert ns.authority == "xxx"
    assert ns.uuid == None

