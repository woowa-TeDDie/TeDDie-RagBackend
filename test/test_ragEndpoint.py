import pytest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_search_endpoint_exists():
    response = client.post("/api/search", json={"query": "test query"})
    assert response.status_code != 404
    assert response.status_code == 200
    
def test_search_returns_list_of_results():
    payload = {"query": "자동차 경주"}
    resp = client.post("/api/search", json=payload)
    data = resp.json()
    
    assert "query" in data
    results = data["results"]
    assert isinstance(results, list)
    assert len(results) > 0 
    
    first = results[0]
    for field in ["repo", "text", "url", "similarity_score"]:
        assert field in first
    assert first["repo"].startswith("java-")
    assert 0 <= first["similarity_score"] <= 1