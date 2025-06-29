
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    title:str
    author:str
    description:Optional[str]=None
    rating:int

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/about")
def get_about():
    return {"message": "About page"}

# Path Parameters
@app.get("/greet/{name}")
async def greet(name:str) -> dict:
    return {"message": f"Hello {name}"}

# Query Parameters
@app.get("/greet1/{name}")
async def greet_name(name:str,age:Optional[int]=None) -> dict:
    return {"message":f"Hello My name is {name} & the age is {age}"}


@app.post("/create-book")
async def create_book(book:Book)->dict:
    new_book = {
        "title":"The Great Gatsby",
        "author":"John Doe",
        "description":"This is a description",
        "rating":11
    }


    return {"message":"Book created", "book":new_book}