#!/usr/bin/env python3
"""
Script to run the Bear AI Brand Mentions API (Stage 2)
"""

import uvicorn
from api import app

if __name__ == "__main__":
    print("🚀 Starting Bear AI Brand Mentions API (Stage 2)")
    print("=" * 50)
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔗 API Endpoints:")
    print("   GET  /mentions      - Get total mentions for all brands")
    print("   GET  /mentions/{brand} - Get mentions for specific brand")
    print("   POST /load-data     - Load Stage 1 data into database")
    print("=" * 50)
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 