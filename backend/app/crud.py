from sqlalchemy.orm import Session
from . import models, schemas

def get_session(db: Session, session_id: int):
    return db.query(models.Session).filter(models.Session.id == session_id).first()

def create_session(db: Session, session: schemas.SessionCreate):
    db_session = models.Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def edit_message(db: Session, message_id: int, new_message: str):
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if db_message:
        db_message.is_edited = True
        db_message.original_message = db_message.message
        db_message.message = new_message
        db.commit()
        db.refresh(db_message)
    return db_message

def delete_message(db: Session, message_id: int):
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if db_message:
        db_message.is_deleted = True
        db.commit()
    return db_message
