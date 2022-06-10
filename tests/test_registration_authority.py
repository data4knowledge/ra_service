import pytest
from model.registration_authority import *
from uuid import uuid4

def test_registration_authority_ror():
  uuid = str(uuid4())
  params = { 'name': 'Jack', 'namespace': uuid, 'ror': {'identifier': 'xxx'} }
  item = RegistrationAuthorityIn(**params)
  assert item.name == "Jack"
  assert item.namespace == uuid
  assert item.ror == {'identifier': 'xxx'} 
  assert item.grid == None
  assert item.company == None
  assert item.dun == None

def test_registration_authorit_dun():
  uuid = str(uuid4())
  params = { 'name': 'Jack', 'namespace':  uuid, 'dun': {'identifier': '123456789'} }
  item = RegistrationAuthorityIn(**params)
  assert item.name == "Jack"
  assert item.namespace == uuid
  assert item.dun == {'identifier': '123456789'} 
  assert item.ror == None
  assert item.company == None
  assert item.grid == None

def test_registration_authorit_grid():
  uuid = str(uuid4())
  params = { 'name': 'Jack', 'namespace':  uuid, 'grid': {'identifier': 'xxx'} }
  item = RegistrationAuthorityIn(**params)
  assert item.name == "Jack"
  assert item.namespace == uuid
  assert item.grid == {'identifier': 'xxx'} 
  assert item.ror == None
  assert item.company == None
  assert item.dun == None

def test_registration_authorit_company():
  uuid = str(uuid4())
  params = { 'name': 'Jack', 'namespace':  uuid, 'company': {'identifier': 'xxx', 'country_code': 'GBR'} }
  item = RegistrationAuthorityIn(**params)
  assert item.name == "Jack"
  assert item.namespace == uuid
  assert item.grid == None
  assert item.ror == None
  assert item.company == {'identifier': 'xxx', 'country_code': 'GBR'} 
  assert item.dun == None

def test_registration_authorit_company_error():
  uuid = str(uuid4())
  params = { 'name': 'Jack', 'namespace': uuid, 'company': {'identifier': 'xxx', 'country_code': 'GB'} }
  with pytest.raises(ValueError):
    item = RegistrationAuthorityIn(**params)

def test_registration_authorit_dun_error():
  uuid = str(uuid4())
  params = { 'name': 'Jack', 'namespace': uuid, 'dun': {'identifier': '12345678'} }
  with pytest.raises(ValueError):
    item = RegistrationAuthorityIn(**params)