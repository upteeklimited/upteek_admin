from typing import Optional, List
from fastapi import APIRouter, Request, Depends, HTTPException, File, UploadFile, Form, Query
from database.db import get_session, get_db
from sqlalchemy.orm import Session
from modules.authentication.auth import auth
from modules.users.merchant import remove_merchant, retrieve_merchants, retrieve_single_merchant, retrieve_merchants_stats, retrieve_single_merchant_stats
from database.schema import MerchantInfoModel, MerchantInfoResponseModel, MerchantStatResponse, MerchantSingleStatResponse, ErrorResponse, PlainResponse
from fastapi_pagination import LimitOffsetPage, Page

router = APIRouter(
    prefix="/merchants",
    tags=["merchants"]
)

@router.get("/delete/{merchant_id}", response_model=PlainResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def single_address(request: Request, db: Session = Depends(get_db), merchant_id: int = 0):
    return remove_merchant(db=db, merchant_id=merchant_id)

@router.get("/", response_model=Page[MerchantInfoModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), user_id: int = Query(None), category_id: int = Query(None), currency_id: int = Query(None), name: str = Query(None), slug: str = Query(None), status: int = Query(None)):
    filters = {}
    if user_id:
        filters['user_id'] = user_id
    if category_id:
        filters['category_id'] = category_id
    if currency_id:
        filters['currency_id'] = currency_id
    if name:
        filters['name'] = name
    if slug:
        filters['slug'] = slug
    if status:
        filters['status'] = status
    return retrieve_merchants(db=db, filters=filters)

@router.get("/get_single/{merchant_id}", response_model=MerchantInfoResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, db: Session = Depends(get_db), merchant_id: int = 0):
    return retrieve_single_merchant(db=db, merchant_id=merchant_id)

@router.get("/statistics", response_model=MerchantStatResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def statistics(request: Request, db: Session = Depends(get_db)):
    return retrieve_merchants_stats(db=db)

@router.get("/statistics/get_single/{merchant_id}", response_model=MerchantInfoResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def statistics_get_single(request: Request, db: Session = Depends(get_db), merchant_id: int = 0):
    return retrieve_single_merchant_stats(db=db, merchant_id=merchant_id)
