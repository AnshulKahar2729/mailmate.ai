from fastapi import APIRouter

router = APIRouter()

@router.get("/latest")
def get_latest_emails():
    return {"emails": ["Email 1", "Email 2", "Email 3"]}
