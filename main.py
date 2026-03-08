from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# CORS add பண்ணு!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    price: float = Field(gt=0)
    available: bool = True

books: List[dict] = [
    {"id": 1, "title": "Python Basics", "author": "Robert", "price": 299, "available": True},
    {"id": 2, "title": "FastAPI Guide", "author": "Kumar", "price": 399, "available": True},
    {"id": 3, "title": "Web Dev", "author": "Praba", "price": 199, "available": False},
]

@app.get("/books")
def get_books():
    return {"books": books}

@app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump())
    return {"msg": "Book added!", "data": book}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found!")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {"msg": f"Book {book_id} deleted!"}
    raise HTTPException(status_code=404, detail="Book not found!")
