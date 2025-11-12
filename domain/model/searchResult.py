from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    repo: str
    text: str
    url: str
    similarity_score: float