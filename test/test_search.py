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
    
def test_search_rejects_empty_query():
    payload = {"query": ""}
    resp = client.post("/api/search", json=payload)
    
    assert resp.status_code == 422
    assert "query" in resp.text
    
def test_search_rejects_top_k_out_of_range():
    invalid_cases = [{"query": "자동차 경주", "top_k": 0},
                    {"query": "자동차 경주", "top_k": 11}]    
    for payload in invalid_cases:
        resp = client.post("/api/search", json=payload)
        
        assert resp.status_code == 422
        
def test_search_rejects_wrong_type():
    payload = {"query": "자동차 경주", "top_k": "three"}
    resp = client.post("/api/search", json=payload)
    assert resp.status_code == 422
    
def test_search_accepts_valid_payload():
    payload = {"query": "자동차 경주", "top_k": 3}
    resp = client.post("/api/search", json=payload)
    
    assert resp.status_code == 200
    
    data = resp.json()
    
    assert data["query"] == "자동차 경주"
    assert len(data["results"]) <= 5