from fastapi import APIRouter, Request, Depends, HTTPException, Query
from modules.authentication.auth import auth
from modules.inventories.groups import retrieve_groups, retrieve_single_group
from database.schema import ErrorResponse, PlainResponse, GroupModel, GroupResponse
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page

router = APIRouter(
    prefix="/inventory/groups",
    tags=["inventory_group"]
)

@router.get("/get_all", response_model=Page[GroupModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), name: str = Query(None), status: int = Query(None), created_by: int = Query(None), merchant_id: int = Query(None)):
    filters = {}
    if name:
        filters['name'] = name
    if status:
        filters['status'] = status
    if created_by:
        filters['created_by'] = created_by
    if merchant_id:
        filters['merchant_id'] = merchant_id
    return retrieve_groups(db=db, filters=filters)

@router.get("/get_single/{group_id}", response_model=GroupResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), group_id: int = 0):
    return retrieve_single_group(db=db, id=group_id)
