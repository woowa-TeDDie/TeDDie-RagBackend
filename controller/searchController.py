from fastapi import APIRouter, HTTPException, Depends
from domain.model.searchRequest import SearchRequest
from domain.model.searchResponse import SearchResponse
from api.service.rag_service import RagSearchService

router = APIRouter(prefix="/api", tags=["Search"])

@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest, rag_service: RagSearchService = Depends()):
    try:
        return service.search(request)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"[Error] 내부 오류 : {e}")