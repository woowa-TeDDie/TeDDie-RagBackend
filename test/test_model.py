import pytest
from pydantic import ValidationError
from api.model import SearchRequest, SearchResult

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