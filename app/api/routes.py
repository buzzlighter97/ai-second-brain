from fastapi import APIRouter
from app.services.note_service import generate_summary
from app.services.prompt_service import response_on_prompt

router = APIRouter()

@router.post("/summarize")
async def summarize_note(note: dict):
    return {"summary": generate_summary(note["text"])}

@router.post("/prompt")
async def make_prompt(prompt: dict):
    return {"response": response_on_prompt(prompt["text"])}

