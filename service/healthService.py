from domain.model.health import HealthResponse
from infra.dependencies import get_rag_system
from datetime import datetime

class HealthService:
    def __init__(self):
        self.rag = get_rag_system()

    def get_status(self) -> HealthResponse:
        index_loaded = getattr(self.rag, "index", None) is not None
        return HealthResponse(
            status="healthy",
            timestamp=datetime.now().isoformat(timespec="seconds"),
            index_loaded=index_loaded
        )
