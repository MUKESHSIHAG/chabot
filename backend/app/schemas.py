from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class MessageBase(BaseModel):
    message: str

class MessageCreate(MessageBase):
    session_id: UUID

class MessageResponse(BaseModel):
    id: UUID
    message: str
    response: str
    timestamp: datetime

    class Config:
        orm_mode = True

class MessageEdit(BaseModel):
    new_message: str

class SessionCreate(BaseModel):
    user_id: Optional[str]

class SessionResponse(BaseModel):
    id: UUID
    start_time: datetime
    end_time: Optional[datetime]
    messages: List[MessageResponse] = []

    class Config:
        orm_mode = True
