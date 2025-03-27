from typing import Dict
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, DECIMAL, Float, TIMESTAMP, SmallInteger, Text, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.schema import ForeignKey
from database.db import Base, get_laravel_datetime, get_added_laravel_datetime, compare_laravel_datetime_with_today
from sqlalchemy.orm import relationship


class AuthToken(Base):

    __tablename__ = "auth_tokens"
     
    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, default=0)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    token_type = Column(String, nullable=True)
    token_value = Column(String, nullable=True)
    status = Column(SmallInteger, default=0)
    expired_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())


def create_auth_token(db: Session, user_id: int = 0, email: str = None, phone_number: str = None, token_type: str = None, token_value: str = None, status: int = 0, expired_at: str = None):
    auth_token = AuthToken(user_id=user_id, email=email, phone_number=phone_number, token_type=token_type, token_value=token_value, status=status, expired_at=expired_at, created_at=get_laravel_datetime(), updated_at=get_laravel_datetime())
    db.add(auth_token)
    db.flush()
    return auth_token

def update_auth_token(db: Session, id: int=0, values: Dict={}):
    values['updated_at'] = get_laravel_datetime()
    db.query(AuthToken).filter_by(id = id).update(values)
    db.flush()
    return True

def delete_auth_token(db: Session, id: int=0):
    values = {
        'updated_at': get_laravel_datetime(),
        'deleted_at': get_laravel_datetime(),
    }
    db.query(AuthToken).filter_by(id = id).update(values)
    db.flush()
    return True

def force_delete_auth_token(db: Session, id: int=0):
    db.query(AuthToken).filter_by(id = id).delete()
    db.flush()
    return True

def get_single_auth_token_by_id(db: Session, id: int=0):
    return db.query(AuthToken).filter_by(id = id).first()

def get_auth_tokens(db: Session):
    return db.query(AuthToken).filter(AuthToken.deleted_at == None).order_by(desc(AuthToken.id))

def get_auth_tokens_by_user_id(db: Session, user_id: int = 0):
    return db.query(AuthToken).filter_by(user_device_id = user_id).filter(AuthToken.deleted_at == None).order_by(desc(AuthToken.id))

def get_latest_user_auth_token(db: Session, user_id: int = 0):
    return db.query(AuthToken).filter_by(user_id = user_id).filter(AuthToken.deleted_at == None).order_by(desc(AuthToken.id)).first()
