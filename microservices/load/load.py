from fastapi import FastAPI

app = FastAPI()

@app.post("/api/load/")
def load(data: dict) -> str:
    print(f"Loading data: {data}")
    result = f"Data with id {data['id']} loaded to osdu"
    return result