from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books: list[Book] = []


@app.get("/books", response_model=list[Book])
def list_books():
    return books


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def add_book(book_input: BookInput):
    # Create a Book with a unique ID, add it to books, and return it.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # Find and return the requested book, or raise an HTTP 404 error.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # Replace the requested book's title and author, or raise HTTP 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # Remove the requested book, or raise HTTP 404.
    raise NotImplementedError