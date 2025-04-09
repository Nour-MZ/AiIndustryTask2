from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
sentiment_model = pipeline("sentiment-analysis")

@app.post("/analyze/")
async def analyze_sentiment(text: str):
    result = sentiment_model(text)
    return result