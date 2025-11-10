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

def test_health_contains_index_loaded_field():
    client = TestClient(app)
    response = client.get("/health")
    data = response.json()
    
    assert "index_loaded" in data
    assert data["index_loaded"] is True
    
def test_health_returns_false_when_index_not_loaded():
    from api.dependencies import get_rag_system
    mock_rag = get_rag_system()
    mock_rag.engine = None
    
    client = TestClient(app)
    response = client.get("/health")
    data = response.json()
    
    assert data["index_loaded"] is False

def test_health_returns_true_when_index_loaded(monkeypatch):
    """RAG 인덱스가 이미 로드된 경우"""
    from api.dependencies import get_rag_system
    mock_rag = get_rag_system()

    class DummyEngine:
        index = True

    mock_rag.engine = DummyEngine()

    client = TestClient(app)
    response = client.get("/health")
    data = response.json()

    assert data["index_loaded"] is True
