# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, DevOps"}

def test_add():
    response = client.get("/add?a=3&b=4")
    assert response.json()["result"] == 7

# add to tests/test_main.py
def test_health():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}