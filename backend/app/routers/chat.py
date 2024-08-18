from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database
import os
from groq import Groq
from dotenv import load_dotenv
from uuid import UUID

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
groq_model = os.environ.get("groq_model")

client = Groq(
    api_key=os.environ.get(GROQ_API_KEY)
)

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat/", response_model=schemas.MessageResponse)
async def chat(message: schemas.MessageCreate, db: Session = Depends(get_db)):   
    print("here is the id....", message, message.session_id)
    session = crud.get_session(db, message.session_id)
    if session is None:
        # Create a new session if it doesn't exist
        session_data = schemas.SessionCreate(user_id="default_user")
        session = crud.create_session(db, session_data)
        message.session_id = session.id

    # Later we can use caching, so added if/else condition and currently set the cached response to False
    cached_response = False
    if cached_response:
        response = cached_response
    else:
        groq_res = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message.message,
                }
            ],
            model=groq_model,
        )
        response = groq_res.choices[0].message.content
    print("res...", response)
    message_data = schemas.MessageCreate(session_id=message.session_id, message=message.message)
    print("msg_data...", message_data)
    db_message = crud.create_message(db, message=message_data)
    db_message.response = response
    db.commit()
    db.refresh(db_message)
    
    return db_message


@router.put("/edit/{message_id}/", response_model=schemas.MessageResponse)
async def edit_message(message_id: UUID, edit: schemas.MessageEdit, db: Session = Depends(get_db)):
    db_message = crud.edit_message(db, message_id, edit.new_message)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@router.delete("/delete/{message_id}/", response_model=schemas.MessageResponse)
async def delete_message(message_id: UUID, db: Session = Depends(get_db)):
    db_message = crud.delete_message(db, message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message