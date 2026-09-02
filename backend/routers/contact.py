import json
import os
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr

from auth import verify_tokens

router = APIRouter()

#simple JSON file (swap for real DB later)
DATA_FILE = os.path.join(os.path.dirname(__file__), "messages.json")

def load_messages() -> list[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_messages(messages:list[dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(messages, f, indent=2)

# --- Request/response models ---
class ContactMessageIn(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    subject: str
    message: str

class ContactMessageOut(ContactMessageIn):
    id: str
    submitted_at: str

# --- Routes --- 
@router.post("/api/contact",response_model=ContactMessageOut)
def submit_contact_message(payload: ContactMessageIn):
    """
    PUBLIC route
    Anyone visiting the site can submit the contact form here.
    """
    messages = load_messages()

    new_message = ContactMessageOut(
        id=str(uuid.uuid4()),
        submitted_at=datetime.now(timezone.utc).isoformat(),
        **payload.model_dump(),
    )

    messages.append(new_message.model_dump())
    save_messages(messages)

    return new_message

@router.get("/api/contact", response_model=list[ContactMessageOut])
def get_contact_messages(user=Depends(verify_tokens)):
    """
    PRIVATE route.
    Only authenticated users can access this route to view submitted contact messages.
    """
    return load_messages()

@router.delete("/api/contact/{message_id}")
def delete_contact_message(message_id: str, user=Depends(verify_tokens)):
    messages = load_messages()

    filtered = [m for m in messages if m["id"] != message_id]

    if len(filtered) == len(messages):
        raise HTTPException(status_code=404, detail="Message not found")

    save_messages(filtered)
    return {"message": "Deleted successfully"}