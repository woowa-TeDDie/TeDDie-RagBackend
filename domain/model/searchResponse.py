from pydantic import BaseModel, Field
from domain.model.searchResult import SearchResult

class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]