from fastapi import APIRouter
from src.book.schemas import Book
from src.book.book_data import books

book_router = APIRouter(
    prefix="",
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)



# GET ALL BOOKS
@book_router.get("/books",response_model=list[Book],status_code=200)
async def get_books()->list:
    return books




# CREATE A BOOK
@book_router.post("/book",status_code=201)
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
@book_router.get("/book/{book_id}")
async def get_single_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message":"Book not found"}




# DELETE A BOOK
@book_router.delete("/book/{book_id}")
async def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message":"Book deleted successfully"}
    return {"message":"Book not found"}



# UPDATE A BOOK
@book_router.put("/book/{book_id}")
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