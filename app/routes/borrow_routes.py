
from fastapi import APIRouter, HTTPException
from datetime import date, timedelta
from app.models.schemas import IssueBook, ReturnBook
from app.database.db import borrow_records
from app.services.library_service import find_member, find_book

router = APIRouter()

@router.post("/issue-book")
def issue_book(data: IssueBook):

    member = find_member(data.member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    book = find_book(data.book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if book["available_copies"] <= 0:
        raise HTTPException(
            status_code=400,
            detail="No copies available"
        )

    issue_date = date.today()
    due_date = issue_date + timedelta(days=7)

    record = {
        "id": len(borrow_records) + 1,
        "member_id": data.member_id,
        "book_id": data.book_id,
        "issue_date": str(issue_date),
        "due_date": str(due_date),
        "return_date": None,
        "late_fee": 0,
        "status": "Issued"
    }

    borrow_records.append(record)

    book["available_copies"] -= 1

    return {
        "success": True,
        "message": "Book issued successfully",
        "data": record
    }

@router.post("/return-book")
def return_book(data: ReturnBook):

    for record in borrow_records:

        if (
            record["member_id"] == data.member_id and
            record["book_id"] == data.book_id and
            record["status"] == "Issued"
        ):

            today = date.today()
            due_date = date.fromisoformat(record["due_date"])

            late_days = (today - due_date).days

            late_fee = 0

            if late_days > 0:
                late_fee = late_days * 10

            record["return_date"] = str(today)
            record["late_fee"] = late_fee
            record["status"] = "Returned"

            book = find_book(data.book_id)

            if book:
                book["available_copies"] += 1

            return {
                "success": True,
                "message": "Book returned successfully",
                "late_fee": late_fee,
                "data": record
            }

    raise HTTPException(
        status_code=404,
        detail="Borrow record not found"
    )

@router.get("/summary/{member_id}")
def member_summary(member_id: int):

    member = find_member(member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    issued_books = 0
    returned_books = 0
    active_books = 0
    total_late_fee = 0

    for record in borrow_records:

        if record["member_id"] == member_id:

            issued_books += 1

            if record["status"] == "Returned":
                returned_books += 1

            if record["status"] == "Issued":
                active_books += 1

            total_late_fee += record["late_fee"]

    return {
        "success": True,
        "member_id": member_id,
        "issued_books": issued_books,
        "returned_books": returned_books,
        "active_books": active_books,
        "total_late_fee": total_late_fee
    }
