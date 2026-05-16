
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class Member(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: EmailStr
    city: str
    membership_status: str

class Book(BaseModel):
    title: str
    author: str
    category: str
    price: float = Field(gt=0)
    available_copies: int = Field(ge=0)

class IssueBook(BaseModel):
    member_id: int
    book_id: int

class ReturnBook(BaseModel):
    member_id: int
    book_id: int
