
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/about")
def get_about():
    return {"message": "About page"}