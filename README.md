# Bear AI Technical Take-Home Assignment

A full-stack system to analyze brand mentions from ChatGPT responses and expose metrics via API.

## 🎯 Project Overview

This project consists of two stages:
- **Stage 1**: Web scraping ChatGPT with sportswear prompts and counting brand mentions
- **Stage 2**: FastAPI server with PostgreSQL database to expose brand mention metrics

## 📋 Requirements

- Python 3.8+
- PostgreSQL database
- Chrome browser (for web scraping)

## 🚀 Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone <repository-url>
cd bear-ai
pip install -r requirements.txt
```

### 2. Database Setup

#### Option A: Local PostgreSQL
```bash
# Install PostgreSQL locally
# Create database
createdb bear_ai_db

# Set environment variable
export DATABASE_URL="postgresql://localhost/bear_ai_db"
```

#### Option B: Supabase (Recommended)
1. Create a Supabase project
2. Get your database connection string
3. Set environment variable:
```bash
export DATABASE_URL="postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres"
```

### 3. Environment Configuration

Create a `.env` file:
```bash
cp env_example.txt .env
# Edit .env with your database URL
```

## 🏃‍♂️ How to Run

### Stage 1: Web Scraping

```bash
# Run the web scraper
python stage1_scraper.py
```

This will:
- Query ChatGPT with 10 sportswear prompts
- Count mentions of Nike, Adidas, Hoka, New Balance
- Save results to `brand_mentions_results.json`

### Stage 2: API Server

```bash
# Start the API server
python run_api.py
```

The API will be available at:
- **API Documentation**: http://localhost:8000/docs
- **API Base URL**: http://localhost:8000

## 🔗 API Endpoints

### GET `/mentions`
Returns total mentions for all brands.

**Example Response:**
```json
{
  "total_mentions": {
    "Nike": 15,
    "Adidas": 12,
    "Hoka": 8,
    "New Balance": 10
  },
  "total_records": 10,
  "brands_tracked": ["Nike", "Adidas", "Hoka", "New Balance"]
}
```

### GET `/mentions/{brand}`
Returns mentions for a specific brand.

**Example Response:**
```json
{
  "brand": "Nike",
  "total_mentions": 15,
  "total_records": 10
}
```

### POST `/load-data`
Loads Stage 1 data into the database.

**Example Response:**
```json
{
  "message": "Successfully loaded 10 records from Stage 1",
  "records_loaded": 10
}
```

## 📊 Example Output

### Stage 1 Output (`brand_mentions_results.json`)
```json
[
  {
    "prompt_id": 1,
    "prompt": "What are the best running shoes in 2025?",
    "response_length": 1250,
    "brand_mentions": {
      "Nike": 3,
      "Adidas": 2,
      "Hoka": 1,
      "New Balance": 0
    },
    "timestamp": "2024-01-15T10:30:00"
  }
]
```

### Stage 2 API Response
```json
{
  "total_mentions": {
    "Nike": 25,
    "Adidas": 18,
    "Hoka": 12,
    "New Balance": 15
  },
  "total_records": 10,
  "brands_tracked": ["Nike", "Adidas", "Hoka", "New Balance"]
}
```

## 🧪 Testing

Run the test script to verify functionality:
```bash
python test_stage1.py
```

## 📁 Project Structure

```
bear-ai/
├── stage1_scraper.py      # Main web scraping script
├── api.py                 # FastAPI application
├── api_routes.py          # API route definitions
├── api_handlers.py        # API business logic
├── database.py            # Database models and connection
├── config.py              # Configuration constants
├── utils.py               # Utility functions
├── run_api.py             # API server runner
├── test_stage1.py         # Test script
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment configuration example
└── README.md              # This file
```

## 🔧 Technical Details

- **Web Scraping**: Selenium with Chrome WebDriver
- **API Framework**: FastAPI
- **Database**: PostgreSQL (as required)
- **ORM**: SQLAlchemy
- **File Structure**: Modular design with files < 100 lines each

## 🚀 Suggestions for Improvements

1. **Authentication**: Add API key authentication
2. **Rate Limiting**: Implement request rate limiting
3. **Caching**: Add Redis caching for API responses
4. **Monitoring**: Add logging and metrics collection
5. **Scaling**: Containerize with Docker for easy deployment
6. **Testing**: Add comprehensive unit and integration tests
7. **Data Pipeline**: Implement scheduled data collection
8. **Analytics**: Add trend analysis and reporting features

## 📞 Questions

For questions about this assignment, contact: sid@usebear.ai 