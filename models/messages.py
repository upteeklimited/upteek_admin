from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime, get_added_laravel_datetime, compare_laravel_datetime_with_today
from sqlalchemy.orm import relationship


class Message(Base):

    __tablename__ = "messages"
     
    id = Column(BigInteger, primary_key=True, index=True)
    sender_user_id = Column(BigInteger, default=0)
    receiver_user_id = Column(BigInteger, default=0)
    previous_message_id = Column(BigInteger, default=0)
    title = Column(String, nullable=True)
    body = Column(Text, nullable=True)
    attached_file = Column(Text, nullable=True)
    status = Column(SmallInteger, default=0)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())

def create_message(db: Session, sender_user_id: int = 0, receiver_user_id: int = 0, previous_message_id: int = 0, title: str = None, body: str = None, attached_file: str = None, status: int = 0):
    message = Message(sender_user_id=sender_user_id, receiver_user_id=receiver_user_id, previous_message_id=previous_message_id, title=title, body=body, attached_file=attached_file, status=status, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(message)
    db.flush()
    return message

def update_message(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(Message).filter_by(id = id).update(values)
    db.flush()
    return True

def delete_message(db: Session, id: int=0):
    values = {
        'updated_at': get_laravel_datetime(),
        'deleted_at': get_laravel_datetime(),
    }
    db.query(Message).filter_by(id = id).update(values)
    db.flush()
    return True

def force_delete_message(db: Session, id: int=0):
    db.query(Message).filter_by(id = id).delete()
    db.flush()
    return True

def get_all_messages(db: Session, filters: Dict={}):
    query = db.query(Message)
    if 'sender_user_id' in filters:
        query = query.filter_by(sender_user_id = filters['sender_user_id'])
    if 'receiver_user_id' in filters:
        query = query.filter_by(receiver_user_id = filters['receiver_user_id'])
    if 'status' in filters:
        query = query.filter_by(status = filters['status'])
    return query.order_by(desc(Message.created_at))
