
from fastapi import APIRouter, HTTPException
from app.models.schemas import Member
from app.database.db import members
from app.services.library_service import find_member

router = APIRouter()

@router.post("/members", status_code=201)
def create_member(member: Member):

    member_data = member.dict()
    member_data["id"] = len(members) + 1

    members.append(member_data)

    return {
        "success": True,
        "message": "Member created successfully",
        "data": member_data
    }

@router.get("/members")
def get_members():
    return {
        "success": True,
        "data": members
    }

@router.get("/members/{member_id}")
def get_member(member_id: int):

    member = find_member(member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return {
        "success": True,
        "data": member
    }
