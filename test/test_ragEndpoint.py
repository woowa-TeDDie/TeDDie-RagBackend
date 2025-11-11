import pytest
from fastapi.testclient import TestClient
from api.app import app

def test_search_endpoint_exists():
    client = TestClient(app)
    response = client.post("/api/search", json={"query": "test query"})
    assert response.status_code != 404
    assert response.status_code == 200