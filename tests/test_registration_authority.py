import pytest
from model.registration_authority import RegistrationAuthority

def test_registration_authority():
    params = { 'name': 'Jack', 'namespace': '12345', 'ror': {'identifier': 'xxx'} }
    item = RegistrationAuthority(**params)
    assert item.name == "Jack"
    assert item.namespace == '12345'
    assert item.ror == {'identifier': 'xxx'} 
    assert item.grid == None
    assert item.company == None
    assert item.dun == None

