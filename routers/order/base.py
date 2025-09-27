from typing import Optional, List, Any
from fastapi import APIRouter, Request, Depends, HTTPException, Query
from modules.authentication.auth import auth
from database.schema import ErrorResponse, PlainResponse, OrderModel, OrderResponse, OrderStatResponse
from modules.orders.get import retrieve_orders, retrieve_single_order, retrieve_order_stats
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from settings.constants import USER_TYPES


router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/get_all", response_model=Page[OrderModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), order_id: int = Query(None), status: int = Query(None), merchant_id: int = Query(None), customer_merchant_id: int = Query(None), user_id: int = Query(None), payment_type: int = Query(None), minimum_amount: float = Query(None), maximum_amount: float = Query(None), from_date: str = Query(None), to_date: str = Query(None), user_query: str = Query(None), reference: str = Query(None)):
    filters = {}
    if order_id:
        filters['order_id'] = order_id
    if status:
        filters['status'] = status
    if merchant_id:
        filters['merchant_id'] = merchant_id
    if customer_merchant_id:
        filters['customer_merchant_id'] = customer_merchant_id
    if user_id:
        filters['user_id'] = user_id
    if payment_type:
        filters['payment_type'] = payment_type
    if minimum_amount:
        filters['minimum_amount'] = minimum_amount
    if maximum_amount:
        filters['maximum_amount'] = maximum_amount
    if from_date:
        filters['from_date'] = from_date
    if to_date:
        filters['to_date'] = to_date
    if user_query:
        filters['user_query'] = user_query
    if reference:
        filters['reference'] = reference
    return retrieve_orders(db=db, filters=filters)

@router.get("/get_single/{order_id}", response_model=OrderResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), order_id: int = 0):
    return retrieve_single_order(db=db, id=order_id)

@router.get("/statistics", response_model=OrderStatResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def statistics(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db)):
    return retrieve_order_stats(db=db)
