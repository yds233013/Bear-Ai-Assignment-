# Bear AI Assignment

This is my submission for the Bear AI technical take-home assignment. The project has two main parts:

1. **Stage 1**: Scraping ChatGPT responses for sportswear brand mentions
2. **Stage 2**: Building an API to serve the brand mention data

## What it does

### Stage 1 - Web Scraping
- Takes 10 different sportswear-related prompts
- Queries ChatGPT website (not the API) using Selenium
- Counts mentions of Nike, Adidas, Hoka, and New Balance
- Saves results to a JSON file

### Stage 2 - API
- FastAPI server with PostgreSQL database
- Endpoints to get brand mention counts
- Loads the scraped data into the database

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL database
- Chrome browser (for web scraping)

### Installation
```bash
# Clone the repo
git clone https://github.com/yds233013/Bear-Ai-Assignment-.git
cd Bear-Ai-Assignment-

# Install dependencies
pip install -r requirements.txt
```

### Database Setup
You'll need a PostgreSQL database. You can either:

**Option 1: Local PostgreSQL**
```bash
createdb bear_ai_db
export DATABASE_URL="postgresql://localhost/bear_ai_db"
```

**Option 2: Supabase (easier)**
1. Create a Supabase project
2. Get your connection string
3. Set: `export DATABASE_URL="postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres"`

### Environment
```bash
cp env_example.txt .env
# Edit .env with your database URL
```

## Running the Project

### Stage 1: Run the scraper
```bash
python stage1_scraper.py
```
This will:
- Query ChatGPT with 10 prompts
- Count brand mentions
- Save to `brand_mentions_results.json`

### Stage 2: Start the API
```bash
python run_api.py
```
The API will be at http://localhost:8000

## API Endpoints

- `GET /mentions` - Get total mentions for all brands
- `GET /mentions/{brand}` - Get mentions for a specific brand  
- `POST /load-data` - Load Stage 1 data into database
- `GET /docs` - Interactive API docs

### Example API Response
```json
{
  "total_mentions": {
    "Nike": 7,
    "Adidas": 6,
    "Hoka": 3,
    "New Balance": 4
  },
  "total_records": 10,
  "brands_tracked": ["Nike", "Adidas", "Hoka", "New Balance"]
}
```

## Project Structure
```
├── stage1_scraper.py      # Main scraping script
├── api.py                 # FastAPI app
├── api_routes.py          # API endpoints
├── api_handlers.py        # Business logic
├── database.py            # Database models
├── config.py              # Configuration
├── utils.py               # Helper functions
├── run_api.py             # Server runner
├── test_stage1.py         # Test script
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## Testing
```bash
python test_stage1.py
```

## Notes
- All files are under 100 lines as requested
- Uses PostgreSQL as required (not SQLite)
- Includes the bonus endpoint `/mentions/{brand}`
- Has proper error handling and documentation

## Questions
Contact: sid@usebear.ai 