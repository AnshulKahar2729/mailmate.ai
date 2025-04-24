# app/api/v1/calendar.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
def get_calendar_events():
    return {"events": ["Meeting with GPT", "Lunch with Python"]}
