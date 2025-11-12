from fastapi import APIRouter, HTTPException, Depends
from domain.model.searchRequest import SearchRequest
from domain.model.searchResponse import SearchResponse
from service.ragService import RagSearchService

router = APIRouter(prefix="/api", tags=["Search"])

@router.post("/search", response_model=SearchResponse)
def search_endpoint(request: SearchRequest, service: RagSearchService = Depends()):
    try:
        return service.search(request)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"[ERROR] 내부 오류: {e}")