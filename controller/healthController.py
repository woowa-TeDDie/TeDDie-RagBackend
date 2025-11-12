from fastapi import APIRouter, Depends
from infra.dependencies import get_rag_system
from datetime import datetime
from domain.model.health import HealthResponse

router = APIRouter()

@router.get("/", tags=["Root"])
def root():
    return {
        "service": "TeDDie Backend",
        "version": "2.0.0",
        "status": "running"
    }

@router.get("/health")
def health_check(rag = Depends(get_rag_system)):
    timestamp = datetime.now().isoformat(timespec="seconds")
    index_loaded = getattr(rag, "engine", None) is not None
    return {
        "status": "healthy",
        "timestamp": timestamp,
        "index_loaded": index_loaded
    }
