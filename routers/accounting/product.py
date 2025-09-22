from fastapi import APIRouter, Request, Depends, Query
from modules.authentication.auth import auth
from modules.accounting.prods import retrieve_financial_products, retrieve_single_financial_product
from database.schema import ErrorResponse, PlainResponse, FinancialProductModel, FinancialProductResponseModel
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import Page

router = APIRouter(
    prefix="/financial_products",
    tags=["financial_products"]
)

@router.get("/", response_model=Page[FinancialProductModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, db: Session = Depends(get_db), name: str = Query(None), status: int = Query(None), country_id: int = Query(None), currency_id: int = Query(None), product_type: int = Query(None), user_type: int = Query(None), individual_compliance_type: int = Query(None), merchant_compliance_type: int = Query(None)):
    filters = {}
    if name:
        filters['name'] = name
    if status:
        filters['status'] = status
    if country_id:
        filters['country_id'] = country_id
    if currency_id:
        filters['currency_id'] = currency_id
    if product_type:
        filters['product_type'] = product_type
    if user_type:
        filters['user_type'] = user_type
    if individual_compliance_type:
        filters['individual_compliance_type'] = individual_compliance_type
    if merchant_compliance_type:
        filters['merchant_compliance_type'] = merchant_compliance_type
    return retrieve_financial_products(db=db, filters=filters)

@router.get("/get_single/{product_id}", response_model=FinancialProductResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), product_id: int = 0):
    return retrieve_single_financial_product(db=db, product_id=product_id)
