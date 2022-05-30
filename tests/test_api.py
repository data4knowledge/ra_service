import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_namespace_ok():
    body = {
        "name": "123",
        "authority": "xxx",
    }
    response = client.post("/namespace", json=body)
    assert response.status_code == 200

def test_add_namespace_ok():
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


