
# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel

# class Book(BaseModel):
#     title:str
#     author:str
#     description:Optional[str]=None
#     rating:int

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


# @app.get("/about")
# def get_about():
#     return {"message": "About page"}

# # Path Parameters
# @app.get("/greet/{name}")
# async def greet(name:str) -> dict:
#     return {"message": f"Hello {name}"}

# # Query Parameters
# @app.get("/greet1/{name}")
# async def greet_name(name:str,age:Optional[int]=None) -> dict:
#     return {"message":f"Hello My name is {name} & the age is {age}"}


# @app.post("/create-book")
# async def create_book(book:Book)->dict:
#     new_book = {
#         "title":"The Great Gatsby",
#         "author":"John Doe",
#         "description":"This is a description",
#         "rating":11
#     }


#     return {"message":"Book created", "book":new_book}




import stat
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
  {
    "id": 1,
    "title": "The Enchanted Forest",
    "author": "Ariana Willow",
    "reviewer": "Jane Doe",
    "rating": 4.5,
    "review": "Magical story with great characters and world-building.",
    "date": "2025-06-26"
  },
  {
    "id": 2,
    "title": "Ocean's Whisper",
    "author": "Liam Shore",
    "reviewer": "Tom Banner",
    "rating": 3.8,
    "review": "A calm and poetic narrative with vivid imagery.",
    "date": "2025-06-24"
  },
  {
    "id": 3,
    "title": "Code of Shadows",
    "author": "Nina Black",
    "reviewer": "Alicia Kim",
    "rating": 4.2,
    "review": "Great thriller with a tech twist. Keeps you guessing!",
    "date": "2025-06-23"
  },
  {
    "id": 4,
    "title": "Dust and Stars",
    "author": "Harvey Quinn",
    "reviewer": "Daniel Roy",
    "rating": 4.9,
    "review": "Beautifully written and emotionally deep. Loved it.",
    "date": "2025-06-22"
  },
  {
    "id": 5,
    "title": "The Silent Pact",
    "author": "Riya Narayan",
    "reviewer": "Sophie Lin",
    "rating": 3.5,
    "review": "Good story but felt a bit slow in the middle.",
    "date": "2025-06-21"
  },
  {
    "id": 6,
    "title": "Frost & Flame",
    "author": "Ethan Cross",
    "reviewer": "Jackie Hill",
    "rating": 4.3,
    "review": "Action-packed with an engaging fantasy world.",
    "date": "2025-06-20"
  },
  {
    "id": 7,
    "title": "Echoes of the Past",
    "author": "Clara Voss",
    "reviewer": "Rohan Mehta",
    "rating": 4.0,
    "review": "A thoughtful journey through memory and time.",
    "date": "2025-06-19"
  },
  {
    "id": 8,
    "title": "Beneath the Iron Sky",
    "author": "Felix Grant",
    "reviewer": "Lena Carter",
    "rating": 3.9,
    "review": "Dark, gritty, and real. Excellent dystopian fiction.",
    "date": "2025-06-18"
  },
  {
    "id": 9,
    "title": "Letters to the Moon",
    "author": "Maya Thorne",
    "reviewer": "Aditya Sinha",
    "rating": 4.7,
    "review": "Tender and poetic. Perfect for night-time reading.",
    "date": "2025-06-17"
  },
  {
    "id": 10,
    "title": "City of Mirage",
    "author": "Noah Fields",
    "reviewer": "Emily Raye",
    "rating": 4.1,
    "review": "Fast-paced and full of intrigue. Loved the twists.",
    "date": "2025-06-16"
  }
]

class Book(BaseModel):
    id:int
    title:str
    author:str
    reviewer:str
    rating:float
    review:str
    date:str




# GET ALL BOOKS
@app.get("/books",response_model=list[Book],status_code=200)
async def get_books()->list:
    return books




# CREATE A BOOK
@app.post("/book",status_code=201)
async def create_book(book_data:Book):
    new_book = {
        "id":len(books)+1,
        "title":book_data.title,
        "author":book_data.author,
        "reviewer":book_data.reviewer,
        "rating":book_data.rating,
        "review":book_data.review,
        "date":book_data.date
    }
    books.append(new_book)
    return {"message":"Book created successfully", "book":new_book}




# GET A SINGLE BOOK
@app.get("/book/{book_id}")
async def get_single_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message":"Book not found"}




# DELETE A BOOK
@app.delete("/book/{book_id}")
async def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message":"Book deleted successfully"}
    return {"message":"Book not found"}



# UPDATE A BOOK
@app.put("/book/{book_id}")
async def update_book(book_id:int,book_data:Book):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["reviewer"] = book_data.reviewer
            book["rating"] = book_data.rating
            book["review"] = book_data.review
            book["date"] = book_data.date 
            return {"message":"Book updated successfully","book":book}
        else:
            return {"message":"Book not found"}   
