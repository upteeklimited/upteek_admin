from typing import Optional, List, Any
from fastapi import APIRouter, Request, Depends, HTTPException, Query
from modules.authentication.auth import auth
from database.schema import ErrorResponse, PlainResponse, CreateOrderRequest, UpdateOrderRequest, OrderModel, OrderMainModel, NewOrderResponse, OrderResponse
from modules.orders.get import retrieve_orders, retrieve_single_order
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from settings.constants import USER_TYPES


router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/get_all", response_model=Page[OrderModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), status: int = Query(None), merchant_id: int = Query(None), customer_merchant_id: int = Query(None), user_id: int = Query(None)):
    filters = {}
    if status:
        filters['status'] = status
    if merchant_id:
        filters['merchant_id'] = merchant_id
    if customer_merchant_id:
        filters['customer_merchant_id'] = customer_merchant_id
    if user_id:
        filters['user_id'] = user_id
    return retrieve_orders(db=db, filters=filters)

@router.get("/get_single/{order_id}", response_model=OrderResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), order_id: int = 0):
    return retrieve_single_order(db=db, id=order_id)
