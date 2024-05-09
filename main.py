from fastapi import FastAPI
from model import preprocess

app = FastAPI()

@app.get('/')
def read_root():
    return {'hello':'world'}

@app.post("/preprocess")
def preprocess_data(data: dict):
    preprocessed_data = preprocess(data)
    return {"preprocessed_data": preprocessed_data}
