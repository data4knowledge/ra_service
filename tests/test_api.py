import pytest
from fastapi.testclient import TestClient
from main import app
from uuid import uuid4

client = TestClient(app)

def test_add_namespace_ok():
  body = {
      "name": "123",
      "authority": "xxx",
  }
  response = client.post("/namespace", json=body)
  assert response.status_code == 200

def test_add_namespace_error_1():
  body = {
      "name": "123",
  }
  response = client.post("/namespace", json=body)
  assert response.status_code == 422
  assert response.json() == {
      'detail': [{
          'loc': ['body', 'authority'],
          'msg': 'field required',
          'type': 'value_error.missing'
      }]
  }

def test_add_namespace_error_2():
  body = {
      "authority": "123",
  }
  response = client.post("/namespace", json=body)
  assert response.status_code == 422
  assert response.json() == {
      'detail': [{
          'loc': ['body', 'name'],
          'msg': 'field required',
          'type': 'value_error.missing'
      }]
  }

def test_add_ra_ok_1():
  body = { 'name': 'Jack', 'namespace': str(uuid4()), 'company': {'identifier': 'xxx', 'country_code': 'GBR'} }
  response = client.post("/registration_authority", json=body)
  assert response.status_code == 200

def test_add_ra_ok_2():
  body = { 'name': 'Jack', 'namespace': str(uuid4()), 'dun': {'identifier': '123456789'} }
  response = client.post("/registration_authority", json=body)
  assert response.status_code == 200

def test_add_ra_ok_3():
  body = { 'name': 'Jack', 'namespace': str(uuid4()), 'grid': {'identifier': '12345678'} }
  response = client.post("/registration_authority", json=body)
  assert response.status_code == 200

def test_add_ra_ok_4():
  body = { 'name': 'Jack', 'namespace': str(uuid4()), 'ror': {'identifier': '12345678'} }
  response = client.post("/registration_authority", json=body)
  assert response.status_code == 200

def test_add_ra_error_1():
  body = { 'name': 'Jack', 'namespace': str(uuid4()), 'company': {'identifier': 'xxx', 'country_code': 'G'} }
  response = client.post("/registration_authority", json=body)
  assert response.status_code == 422
  assert response.json() == {
    'detail': [{
      'loc': ['body', 'company', 'country_code'],
      'msg': 'must ba a valid ISO 3166 code',
      'type': 'value_error'
    }]
  }

def test_add_ra_error_2():
  body = { 'name': 'Jack', 'namespace': str(uuid4()), 'dun': {'identifier': 'xxx'} }
  response = client.post("/registration_authority", json=body)
  assert response.status_code == 422
  assert response.json() == {
    'detail': [{
      'loc': ['body', 'dun', 'identifier'],
      'msg': 'must ba a 9 digit string',
      'type': 'value_error'
    }]
  }