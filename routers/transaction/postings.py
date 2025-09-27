from typing import List
from fastapi import APIRouter, Request, Depends, HTTPException, Query
from modules.authentication.auth import auth
from modules.postings.trans import retrieve_accounts,  retrieve_transactions, retrieve_transaction_by_id, retrieve_stats
from database.schema import ErrorResponse, PlainResponse, TransactionAccountModel, TransactionModel, TransactionResponseModel, TransactionStatResponse
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import Page

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/search_accounts/{search}", response_model=List[TransactionAccountModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def search_accounts(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), search: str = None):
    return retrieve_accounts(db=db, search=search)

@router.get("/", response_model=Page[TransactionModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, db: Session = Depends(get_db), user=Depends(auth.auth_wrapper), transaction_id: int = Query(None), user_id: int = Query(None), merchant_id: int = Query(None), type_id: int = Query(None), action: int = Query(None), reference: str = Query(None), external_reference: str = Query(None), account_number: str = Query(None), account_name: str = Query(None), from_date: str = Query(None), to_date: str = Query(None), minimum_amount: float = Query(None), maximum_amount: float = Query(None), user_query: str = Query(None), status: int = Query(None)):
    filters = {}
    if transaction_id:
        filters['transaction_id'] = transaction_id
    if user_id:
        filters['user_id'] = user_id
    if merchant_id:
        filters['merchant_id'] = merchant_id
    if type_id:
        filters['type_id'] = type_id
    if action:
        filters['action'] = action
    if reference:
        filters['reference'] = reference
    if external_reference:
        filters['external_reference'] = external_reference
    if account_number:
        filters['account_number'] = account_number
    if account_name:
        filters['account_name'] = account_name
    if from_date:
        filters['from_date'] = from_date
    if to_date:
        filters['to_date'] = to_date
    if minimum_amount:
        filters['minimum_amount'] = minimum_amount
    if maximum_amount:
        filters['maximum_amount'] = maximum_amount
    if status:
        filters['status'] = status
    if user_query:
        filters['user_query'] = user_query
    return retrieve_transactions(db=db, filters=filters)

@router.get("/get_single/{transaction_id}", response_model=TransactionResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), transaction_id: int = 0):
    return retrieve_transaction_by_id(db=db, transaction_id=transaction_id)

@router.get("/statistics", response_model=TransactionStatResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def statistics(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db)):
    return retrieve_stats(db=db)
