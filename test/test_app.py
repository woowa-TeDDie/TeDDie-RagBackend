import pytest
from fastapi.testclient import TestClient
from api.app import app

def test_root_endpoint_returns_200():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    
def test_root_endpoint_returns_service_info():
    client = TestClient(app)
    response = client.get("/")
    data = response.json()
    
    assert "service" in data
    assert "version" in data
    assert data["service"] == "TeDDie Backend"