from fastapi import FastAPI
from app.api.v1 import email, calendar, chat

app = FastAPI()

# Register routes
app.include_router(email.router, prefix="/api/v1/email", tags=["Email"])
app.include_router(calendar.router, prefix="/api/v1/calendar", tags=["Calendar"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "FastAPI server is running 🚀"}
