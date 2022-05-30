import pytest
from model.registration_authority import RegistrationAuthority

def test_registration_authority_ror():
    params = { 'name': 'Jack', 'namespace': '12345', 'ror': {'identifier': 'xxx'} }
    item = RegistrationAuthority(**params)
    assert item.name == "Jack"
    assert item.namespace == '12345'
    assert item.ror == {'identifier': 'xxx'} 
    assert item.grid == None
    assert item.company == None
    assert item.dun == None

def test_registration_authorit_dun():
    params = { 'name': 'Jack', 'namespace': '12345', 'dun': {'identifier': '123456789'} }
    item = RegistrationAuthority(**params)
    assert item.name == "Jack"
    assert item.namespace == '12345'
    assert item.dun == {'identifier': '123456789'} 
    assert item.ror == None
    assert item.company == None
    assert item.grid == None

def test_registration_authorit_grid():
    params = { 'name': 'Jack', 'namespace': '12345', 'grid': {'identifier': 'xxx'} }
    item = RegistrationAuthority(**params)
    assert item.name == "Jack"
    assert item.namespace == '12345'
    assert item.grid == {'identifier': 'xxx'} 
    assert item.ror == None
    assert item.company == None
    assert item.dun == None

def test_registration_authorit_company():
    params = { 'name': 'Jack', 'namespace': '12345', 'company': {'identifier': 'xxx', 'country_code': 'GBR'} }
    item = RegistrationAuthority(**params)
    assert item.name == "Jack"
    assert item.namespace == '12345'
    assert item.grid == None
    assert item.ror == None
    assert item.company == {'identifier': 'xxx', 'country_code': 'GBR'} 
    assert item.dun == None

def test_registration_authorit_company_error():
    params = { 'name': 'Jack', 'namespace': '12345', 'company': {'identifier': 'xxx', 'country_code': 'GB'} }
    with pytest.raises(ValueError):
      item = RegistrationAuthority(**params)

def test_registration_authorit_dun_error():
    params = { 'name': 'Jack', 'namespace': '12345', 'dun': {'identifier': '12345678'} }
    with pytest.raises(ValueError):
      item = RegistrationAuthority(**params)


