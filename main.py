from datetime import datetime
import random
from fastapi import FastAPI

app = FastAPI()

with open("data/quotes.txt", "r", encoding="utf-8") as f:
    quotes = f.readlines()


@app.get("/")
async def root(seed: int = None):
    random.seed(datetime.now().timestamp())
    if seed != None:
        random.seed(seed)
    return quotes[random.randint(0, len(quotes) - 1)].strip()
