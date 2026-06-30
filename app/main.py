# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, DevOps"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# add to app/main.py
@app.get("/health")
def health():
    return {"status": "ok"}