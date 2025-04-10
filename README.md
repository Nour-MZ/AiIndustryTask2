# AI Model API Service

## Description
This project deploys a sentiment analysis model as a RESTful API using FastAPI.

## Setup
1. Clone the repository:
  
   git clone <repository-url>
   cd app

2. Install dependencies:

   pip install -r app/requirements.txt


3. Run the API:
   uvicorn app.main:app --reload

4. Usage:
   Send a POST request to /analyze/ with JSON content:

   {
      "text": "Your text here."
   }

