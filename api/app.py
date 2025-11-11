from fastapi import FastAPI, Depends
from api.dependencies import get_rag_system
from rag.RagSearch import WoowacourseRAG
from datetime import datetime
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[INFO] 🚀 TeDDie 백엔드 서버 실행 중...")
    yield
    print("[INFO] 🛑 TeDDie 백엔드 서버 종료 중...")

app = FastAPI(
    title="TeDDie Backend API",
    description="API for TeDDie Backend Service",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {
        "service": "TeDDie Backend",
        "version": "1.0.0",
        "status": "running",
    }

@app.get("/health")
def health_check(rag: WoowacourseRAG = Depends(get_rag_system)):
    index_loaded = rag.index is not None
    timestamp = datetime.now().isoformat(timespec="seconds")

    return {
        "status": "healthy",
        "timestamp": timestamp,
        "index_loaded": index_loaded
    }

@app.post("/api/search")
def search(payload: dict):
    return {"query": payload.get("query", ""), "results": []}
