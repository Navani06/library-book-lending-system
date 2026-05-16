
from fastapi import APIRouter, HTTPException, Query
from app.models.schemas import Book
from app.database.db import books
from app.services.library_service import find_book

router = APIRouter()

@router.post("/books", status_code=201)
def create_book(book: Book):

    book_data = book.dict()
    book_data["id"] = len(books) + 1

    books.append(book_data)

    return {
        "success": True,
        "message": "Book added successfully",
        "data": book_data
    }

@router.get("/books")
def get_books(category: str = Query(default=None)):

    if category:
        filtered_books = []

        for book in books:
            if book["category"].lower() == category.lower():
                filtered_books.append(book)

        return {
            "success": True,
            "data": filtered_books
        }

    return {
        "success": True,
        "data": books
    }

@router.get("/books/{book_id}")
def get_book(book_id: int):

    book = find_book(book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "success": True,
        "data": book
    }
