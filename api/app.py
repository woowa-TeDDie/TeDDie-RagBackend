from fastapi import FastAPI

app = FastAPI(
    title= "TeDDie Backend API",
    description="API for TeDDie Backend Service",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service" : "TeDDie Backend",
        "version" : "1.0.0",
        "status" : "running"
    }
    
@app.get("/health")
def health():
    from datetime import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    
@app.post("/api/search")
def search(payload: dict):
    return {"query": payload.get("query", ""), "results": []}
    