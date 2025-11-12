from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, example="자동차 경주 게임")
    top_k: int = Field(3, ge=1, le=10, example=3)