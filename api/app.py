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