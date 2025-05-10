from fastapi import APIRouter, Request, Depends
from modules.authentication.auth import auth
from modules.miscelleanous.merchant_misc import create_new_merchant_industry, update_existing_merchant_industry, delete_existing_merchant_industry, retrieve_merchant_industries, retrieve_single_merchant_industry, create_new_merchant_category, update_existing_merchant_category, delete_existing_merchant_category, retrieve_merchant_categories, retrieve_single_merchant_category
from database.schema import ErrorResponse, PlainResponse, CreateMerchantIndustryModel, UpdateMerchantIndustryModel, MerchantIndustryModel, MerchantIndustryResponseModel, CreateMerchantCategoryModel, UpdateMerchantCategoryModel, MerchantCategoryModel, MerchantCategoryResponseModel
from database.db import get_session, get_db
from sqlalchemy.orm import Session
from fastapi_pagination import Page

router = APIRouter(
    prefix="/misc",
    tags=["misc"]
)

@router.post("/industries/create", response_model=MerchantIndustryResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def industry_create(request: Request, fields: CreateMerchantIndustryModel, db: Session = Depends(get_db), user=Depends(auth.auth_wrapper)):
    req = create_new_merchant_industry(db=db, name=fields.name, description=fields.description)
    return req

@router.post("/industries/update/{industry_id}", response_model=PlainResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def industry_update(request: Request, fields: UpdateMerchantIndustryModel, db: Session = Depends(get_db), user=Depends(auth.auth_wrapper), industry_id: int=0):
    values = fields.model_dump()
    req = update_existing_merchant_industry(db=db, industry_id=industry_id, values=values)
    return req

@router.get("/industries/delete/{industry_id}", response_model=PlainResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def industry_delete(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), industry_id: int = 0):
    return delete_existing_merchant_industry(db=db, industry_id=industry_id)

@router.get("/industries", response_model=Page[MerchantIndustryModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def industries(request: Request, db: Session = Depends(get_session)):
    return retrieve_merchant_industries(db=db)

@router.get("/industries/get_single/{industry_id}", response_model=MerchantIndustryResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def industries_get_single(request: Request, db: Session = Depends(get_session), industry_id: int = 0):
    return retrieve_single_merchant_industry(db=db, industry_id=industry_id)

@router.post("/categories/create", response_model=MerchantCategoryResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def category_create(request: Request, fields: CreateMerchantCategoryModel, db: Session = Depends(get_db), user=Depends(auth.auth_wrapper)):
    req = create_new_merchant_category(db=db, industry_id=fields.industry_id, name=fields.name, description=fields.description)
    return req

@router.post("/categories/update/{category_id}", response_model=PlainResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def category_update(request: Request, fields: UpdateMerchantCategoryModel, db: Session = Depends(get_db), user=Depends(auth.auth_wrapper), category_id: int=0):
    values = fields.model_dump()
    req = update_existing_merchant_category(db=db, category_id=category_id, values=values)
    return req

@router.get("/categories/delete/{category_id}", response_model=PlainResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def category_delete(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), category_id: int = 0):
    return delete_existing_merchant_category(db=db, category_id=category_id)

@router.get("/categories", response_model=Page[MerchantCategoryModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def categories(request: Request, db: Session = Depends(get_session), industry_id: int = 0):
    filters = {}
    if industry_id is not None:
        if industry_id > 0:
            filters['industry_id'] = industry_id
    return retrieve_merchant_categories(db=db, filters=filters)

@router.get("/categories/get_single/{category_id}", response_model=MerchantCategoryResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def categories_get_single(request: Request, db: Session = Depends(get_session), category_id: int = 0):
    return retrieve_single_merchant_category(db=db, category_id=category_id)
