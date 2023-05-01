from fastapi import FastAPI
from etl import run_etl

app = FastAPI()

@app.get("/api/run-etl/")
def main() -> str:
    return run_etl()