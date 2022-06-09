import pytest
from model.namespace import *

def test_namespace():
    params = {'name': 'Jack', 'authority': 'xxx'}
    ns = NamespaceIn(**params)
    assert ns.name == "Jack"
    assert ns.authority == "xxx"

