"""
Database models and connection for Bear AI Assignment Stage 2
Uses PostgreSQL as recommended in the assignment.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection - using PostgreSQL as required
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/bear_ai_db')

# Create engine with connection timeout and error handling
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Test connections before using
    pool_recycle=300,    # Recycle connections every 5 minutes
    connect_args={"connect_timeout": 10}  # 10 second timeout
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BrandMention(Base):
    """Database model for storing brand mention data"""
    __tablename__ = "brand_mentions"
    
    id = Column(Integer, primary_key=True, index=True)
    prompt_id = Column(Integer, nullable=False)
    prompt = Column(String, nullable=False)
    response_length = Column(Integer, nullable=False)
    brand_mentions = Column(JSON, nullable=False)  # Store as JSON: {"Nike": 2, "Adidas": 1}
    timestamp = Column(DateTime, default=datetime.utcnow)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables initialized successfully")
    except Exception as e:
        print(f"⚠️  Database initialization failed: {e}")
        print("   Make sure PostgreSQL is running and DATABASE_URL is correct")
        print("   You can still run the API, but database operations will fail") 