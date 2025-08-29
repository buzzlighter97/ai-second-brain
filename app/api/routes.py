from fastapi import APIRouter
from app.services.note_service import generate_summary

router = APIRouter()

@router.post("/summarize")
async def summarize_note(note: dict):
    return {"summary": generate_summary(note["text"])}

