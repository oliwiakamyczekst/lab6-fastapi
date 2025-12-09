from fastapi.testclient import TestClient
from main import app

def test_hello():
    client = TestClient(app)
    resp = client.get('/hello')
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello world!"}
