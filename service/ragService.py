from fastapi import Depends, HTTPException
from domain.model.searchRequest import SearchRequest
from domain.model.searchResponse import SearchResponse
from domain.model.searchResult import SearchResult
from util.repository.ragRepository import RagRepository

class RagSearchService:
    def __init__(self, rag_repository: RagRepository = Depends()):
        self.rag_repository = rag_repository

    def search(self, request: SearchRequest) -> SearchResponse:
        if not self.rag_repository.is_index_loaded():
            raise HTTPException(status_code=503, detail="[ERROR] RAG 인덱스가 로드되지 않았습니다.")
        
        try:
            raw_results = self.rag_repository.search_documents(request.query, top_k=request.top_k)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"[ERROR] RAG 검색 실패: {e}")
        
        results = [
            SearchResult(
                repo=item['repo'],
                text=item['text'],
                url=item['url'],
                similarity_score=item['similarity_score']
            ) 
            for item in raw_results
        ]
        return SearchResponse(query=request.query, results=results)