from fastapi import FastAPI
from controller.searchController import router as search_router
from controller.healthController import router as health_router
from util.logger import logger

app = FastAPI(
    title="TeDDie RAG Backend",
    description="RAG 검색 API 서버",
    version="2.0.0"
)

app.include_router(search_router)
app.include_router(health_router)

logger.info("🚀 TeDDie-RagBackend 서버 실행 중")
