# app/api/v1/chat.py

from fastapi import APIRouter

router = APIRouter()

@router.post("/ask")
def ask_ai(prompt: str):
    return {"response": f"Fake AI response to: {prompt}"}
