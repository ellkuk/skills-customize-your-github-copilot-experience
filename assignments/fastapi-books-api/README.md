# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to manage a collection of books. Practice defining request data with Pydantic, creating CRUD endpoints, and returning appropriate HTTP status codes and errors.

## 📝 Tasks

### 🛠️ Create and Add Books

#### Description
Complete the starter app to list all books and add a new book. Each book should have a unique ID, a title, and an author. Install the packages in `requirements.txt`, rename `starter-code.py` to `main.py`, then run the API with `uvicorn main:app --reload`. Use the interactive API documentation at `/docs` to try your endpoints.

#### Requirements
Completed program should:

- Define a Pydantic model that validates a book's title and author
- Implement `GET /books` to return all books
- Implement `POST /books` to add a book and return the created book with a unique ID
- Return HTTP `201 Created` when a book is added


### 🛠️ Complete the Books CRUD API

#### Description
Add endpoints to retrieve, update, and delete one book by its ID. Make the API respond clearly when a requested book does not exist.

#### Requirements
Completed program should:

- Implement `GET /books/{book_id}` to return one book
- Implement `PUT /books/{book_id}` to update a book's title and author
- Implement `DELETE /books/{book_id}` to remove a book
- Return HTTP `404 Not Found` when an ID does not match a book
- Test each endpoint in `/docs`, including an unknown book ID