from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="FastAPI Azure Demo", version="1.0")

@app.get("/")
async def root():
    return {"message": "🚀 FastAPI is running on Azure App Service!"}

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"}, status_code=200)