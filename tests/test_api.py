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


