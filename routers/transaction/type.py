from fastapi import APIRouter, Request, Depends, Query
from modules.authentication.auth import auth
from modules.postings.trans_type import retrive_transaction_type, retrieve_single_transaction_type, retrieve_single_transaction_type_by_code
from database.schema import ErrorResponse, PlainResponse, TransactionTypeModel, TransTypeResponseModel
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import Page

router = APIRouter(
    prefix="/transaction_types",
    tags=["transaction_types"]
)

@router.get("/", response_model=Page[TransactionTypeModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, db: Session = Depends(get_db), name: str = Query(None), code: str = Query(None), action: int = Query(None), chargeable: int = Query(None), charge_type: int = Query(None), require_approval: int = Query(None), is_system: int = Query(None), status: int = Query(None), created_by: int = Query(None)):
    filters = {}
    if action:
        filters['action'] = action
    if name:
        filters['name'] = name
    if code:
        filters['code'] = code
    if status:
        filters['status'] = status
    if created_by:
        filters['created_by'] = created_by
    if chargeable:
        filters['chargeable'] = chargeable
    if charge_type:
        filters['charge_type'] = charge_type
    if require_approval:
        filters['require_approval'] = require_approval
    if is_system:
        filters['is_system'] = is_system
    return retrive_transaction_type(db=db, filters=filters)

@router.get("/get_single/{type_id}", response_model=TransTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), type_id: int = 0):
    return retrieve_single_transaction_type(db=db, type_id=type_id)

@router.get("/get_single_by_code/{code}", response_model=TransTypeResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single_by_code(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), code: str = None):
    return retrieve_single_transaction_type_by_code(db=db, code=code)

