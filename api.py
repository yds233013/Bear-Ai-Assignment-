"""
FastAPI application for Bear AI Assignment Stage 2
Provides API endpoints for brand mention metrics.
"""

from fastapi import FastAPI
from database import init_db
from api_routes import router

app = FastAPI(
    title="Bear AI Brand Mentions API",
    description="API for retrieving brand mention metrics from ChatGPT responses",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Bear AI Brand Mentions API",
        "endpoints": {
            "/mentions": "Get total mentions for all brands",
            "/mentions/{brand}": "Get mentions for specific brand",
            "/load-data": "Load Stage 1 data into database"
        }
    }

# Include the API routes
app.include_router(router) 