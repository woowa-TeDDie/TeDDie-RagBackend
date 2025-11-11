import pytest
from pydantic import ValidationError
from api.model import SearchRequest, SearchResult, SearchResponse

def test_search_request_valid():
    req = SearchRequest(query="로또", top_k=3)
    
    assert req.query == "로또"
    assert req.top_k == 3
    
def test_search_request_default_top_k():
    req = SearchRequest(query="자동차 경주")
    
    assert req.top_k == 3

def test_search_request_empty_query_not_allowed():
    with pytest.raises(ValidationError):
        SearchRequest(query="", top_k=3)
        
def test_search_result_can_be_created():
    result = SearchResult(
        repo = "java-racingcar-6",
        text = "# 미션 - 자동차 경주",
        url = "https://github.com/woowacourse/java-racingcar-6",
        similarity_score = 0.985,
    )
    
    assert result.repo == "java-racingcar-6"
    assert result.similarity_score == 0.985
    
def test_search_response_can_be_created():
    resp = SearchResponse(query = "로또", results = [])
    
    assert resp.query == "로또"
    assert resp.results == []
    
def test_search_response_contains_list_of_results():
    result = SearchResult(
        repo = "java-lotto-6",
        text = "# 미션 - 로또",
        url = "https://github.com/woowacourse/java-lotto-6",
        similarity_score = 0.985,
    )
    resp = SearchResponse(query = "로또", results = [result])
    
    assert resp.results[0].repo == "java-lotto-6"
    assert isinstance(resp.results[0].similarity_score, float)