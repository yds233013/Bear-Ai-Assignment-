"""
API routes for Bear AI Assignment Stage 2
Contains the endpoint handlers for brand mention metrics.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from api_handlers import get_all_brand_mentions, get_specific_brand_mentions, load_stage1_data_to_db

router = APIRouter()

@router.get("/mentions")
async def get_all_mentions(db: Session = Depends(get_db)):
    """Get total number of mentions for each brand"""
    return get_all_brand_mentions(db)

@router.get("/mentions/{brand}")
async def get_brand_mentions(brand: str, db: Session = Depends(get_db)):
    """Get count only for the specified brand"""
    return get_specific_brand_mentions(brand, db)

@router.post("/load-data")
async def load_stage1_data(db: Session = Depends(get_db)):
    """Load data from Stage 1 JSON file into database"""
    return load_stage1_data_to_db(db) 