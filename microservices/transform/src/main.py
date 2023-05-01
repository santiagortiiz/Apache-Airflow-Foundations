from fastapi import FastAPI
from src.mapping.sample import map_schema

app = FastAPI()

@app.post("/api/transform/")
def map_data(prev_result: int, source_data: dict, some_schema: dict) -> dict:
    osdu_data = map_schema(source_data, some_schema)
    osdu_data['id'] = prev_result
    return osdu_data