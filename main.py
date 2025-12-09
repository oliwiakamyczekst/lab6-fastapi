from fastapi import FastAPI
from metrics import request_counter

app = FastAPI()

@app.get("/hello")
def hello():
    request_counter.inc()
    return {"message": "Hello world!"}
