from typing import Optional, List, Any
from fastapi import APIRouter, Request, Depends, HTTPException, File, UploadFile, Form, Query
from modules.authentication.auth import auth
from modules.inventories.products import create_new_product, create_multi_products, upload_product_media, remove_product_media, add_product_categories, sub_product_categories, add_product_groups, sub_product_groups, add_product_tags, remove_product_tags, update_existing_product, update_multiple_products, update_diverse_products, delete_existing_product, retrieve_products, retrieve_single_product, retrieve_single_product_by_slug, favorite_toggle
from database.schema import ErrorResponse, PlainResponse, ProductModel, ProductResponseModel
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page
from settings.constants import USER_TYPES
import json

router = APIRouter(
    prefix="/inventory/products",
    tags=["inventory_product"]
)

@router.get("/get_all", response_model=Page[ProductModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), category_id: int = Query(None), categories: str = Query(None), currency_id: int=Query(None), merchant_id: int=Query(None), name: str = Query(None), status: int = Query(None), top_discount: int = Query(None), created_by: int = Query(None), authorized_by: int = Query(None)):
    filters = {}
    if category_id:
        filters['category_id'] = category_id
    if categories:
        filters['categories'] = json.loads(categories)
    if currency_id:
        filters['currency_id'] = currency_id
    if merchant_id:
        filters['merchant_id'] = merchant_id
    if name:
        filters['name'] = name
    if top_discount:
        filters['top_discount'] = top_discount
    if status:
        filters['status'] = status
    if created_by:
        filters['created_by'] = created_by
    if authorized_by:
        filters['authorized_by'] = authorized_by
    return retrieve_products(db=db, filters=filters)

@router.get("/get_single/{product_id}", response_model=ProductResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, db: Session = Depends(get_db), product_id: int = 0):
    return retrieve_single_product(db=db, id=product_id)

@router.get("/get_single_by_slug/{slug}", response_model=ProductResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_by_slug(request: Request, db: Session = Depends(get_db), slug: str = None):
    return retrieve_single_product_by_slug(db=db, slug=slug)
