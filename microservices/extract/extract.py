import random
from fastapi import FastAPI

app = FastAPI()

def get_random_number(lower_limit=0, upper_limit=10):
    """Return a random number between the specified limits"""
    random_number = random.randint(lower_limit, upper_limit)
    return random_number

@app.get("/api/extract/")
def get_data() -> int:
    return get_random_number()