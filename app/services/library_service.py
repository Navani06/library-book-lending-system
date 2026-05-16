
from app.database.db import members, books, borrow_records

def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None
