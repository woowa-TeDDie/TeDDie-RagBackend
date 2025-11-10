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
    
def test_health_endpoint_returns_200():
    client = TestClient(app)
    response = client.get("/health")
    
    assert response.status_code == 200
    
def test_health_endpoint_contains_status_and_timestamp():
    client = TestClient(app)
    response = client.get("/health")
    data = response.json()
    
    assert "status" in data
    assert "timestamp" in data
    assert data["status"] == "healthy"
