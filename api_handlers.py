"""
API handlers for Bear AI Assignment Stage 2
Contains the business logic for brand mention endpoints.
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
import json
import os

from database import BrandMention
from config import BRANDS

def get_all_brand_mentions(db: Session):
    """Get total number of mentions for each brand"""
    try:
        records = db.query(BrandMention).all()
        
        total_mentions = {brand: 0 for brand in BRANDS}
        
        for record in records:
            brand_data = record.brand_mentions
            for brand, count in brand_data.items():
                if brand in total_mentions:
                    total_mentions[brand] += count
        
        return {
            "total_mentions": total_mentions,
            "total_records": len(records),
            "brands_tracked": BRANDS
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def get_specific_brand_mentions(brand: str, db: Session):
    """Get count only for the specified brand"""
    if brand not in BRANDS:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid brand. Must be one of: {BRANDS}"
        )
    
    try:
        records = db.query(BrandMention).all()
        
        total_count = 0
        for record in records:
            brand_data = record.brand_mentions
            total_count += brand_data.get(brand, 0)
        
        return {
            "brand": brand,
            "total_mentions": total_count,
            "total_records": len(records)
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def load_stage1_data_to_db(db: Session):
    """Load data from Stage 1 JSON file into database"""
    if not os.path.exists('brand_mentions_results.json'):
        raise HTTPException(
            status_code=404, 
            detail="brand_mentions_results.json not found. Run Stage 1 first."
        )
    
    try:
        with open('brand_mentions_results.json', 'r') as f:
            data = json.load(f)
        
        db.query(BrandMention).delete()
        
        for item in data:
            db_record = BrandMention(
                prompt_id=item['prompt_id'],
                prompt=item['prompt'],
                response_length=item['response_length'],
                brand_mentions=item['brand_mentions'],
                timestamp=item['timestamp']
            )
            db.add(db_record)
        
        db.commit()
        
        return {
            "message": f"Successfully loaded {len(data)} records from Stage 1",
            "records_loaded": len(data)
        }
    
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error loading data: {str(e)}") 