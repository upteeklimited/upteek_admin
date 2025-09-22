from fastapi import APIRouter, Request, Depends, Query
from modules.authentication.auth import auth
from modules.accounting.gl_types import retrieve_gl_types, retrieve_single_gl_type, retrieve_single_gl_type_by_code
from database.schema import ErrorResponse, PlainResponse, GLTypeModel, GLTypeResponseModel
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import Page

router = APIRouter(
    prefix="/general_ledger_types",
    tags=["general_ledger_types"]
)


@router.get("/", response_model=Page[GLTypeModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, db: Session = Depends(get_db), name: str = Query(None), account_code: str = Query(None), status: int = Query(None)):
    filters = {}
    if name:
        filters['name'] = name
    if account_code:
        filters['account_code'] = account_code
    if status:
        filters['status'] = status
    return retrieve_gl_types(db=db, filters=filters)

@router.get("/get_single/{type_id}", response_model=GLTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), type_id: int = 0):
    return retrieve_single_gl_type(db=db, gl_type_id=type_id)

@router.get("/get_single_by_code/{code}", response_model=GLTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_by_code(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), code: str = None):
    return retrieve_single_gl_type_by_code(db=db, code=code)

