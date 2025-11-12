from fastapi import APIRouter, HTTPException
from api.domain.model.health import HealthResponse\
from api.service.healtgService import HealthService

router = APIRouter(tags=["Health"])

@router.get("/health", response_model=HealthResponse)
def health_check(service: HealthService = Depends()):
    return service.get_status()