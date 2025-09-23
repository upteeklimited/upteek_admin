from typing import Optional, List
from fastapi import APIRouter, Request, Depends, HTTPException, Form, Query
from database.db import get_session, get_db
from sqlalchemy.orm import Session
from modules.authentication.auth import auth
from modules.users.customer import retrieve_single_user, retrieve_merchants_and_customers, retrieve_reviews, retrieve_single_review
from database.schema import ErrorResponse, PlainResponse, UserInfoModel, UserInfoResponseModel, ReviewModel, ReviewResponseModel
from fastapi_pagination import LimitOffsetPage, Page

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.get("/", response_model=Page[UserInfoModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), username: str = Query(None), email: str = Query(None), phone_number: str = Query(None), query: str = Query(None)):
    filters = {}
    if username:
        filters['username'] = username
    if email:
        filters['email'] = email
    if phone_number:
        filters['phone_number'] = phone_number
    if query:
        filters['query'] = query
    return retrieve_merchants_and_customers(db=db, filters=filters)

@router.get("/get_single/{user_id}", response_model=UserInfoResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, db: Session = Depends(get_db), user_id: int = 0):
    return retrieve_single_user(db=db, id=user_id)

@router.get("/reviews", response_model=Page[ReviewModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def reviews(request: Request, db: Session = Depends(get_db), merchant_id: int = Query(None), product_id: int = Query(None), status: str = Query(None)):
    filters = {}
    if status:
        filters['status'] = status
    return retrieve_reviews(db=db, product_id=product_id, merchant_id=merchant_id, filters=filters)

@router.get("/reviews/get_single/{review_id}", response_model=ReviewResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_review(request: Request, db: Session = Depends(get_db), review_id: int = 0):
    return retrieve_single_review(db=db, review_id=review_id)
