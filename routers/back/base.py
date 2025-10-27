from typing import Optional, List, Any
from fastapi import APIRouter, Request, Depends, HTTPException, Query
from modules.authentication.auth import auth
from database.schema import ErrorResponse, PlainResponse, BatchModel, BatchResponseModel, ContinueBatchModel
from modules.background.batch import retrieve_batches, retrieve_single_batch, continue_batch
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import LimitOffsetPage, Page


router = APIRouter(
    prefix="/batches",
    tags=["batches"]
)

@router.get("/", response_model=Page[BatchModel], responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_all(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), batch_type: int = Query(None), status: int = Query(None), reference: str = Query(None)):
    filters = {}
    if batch_type:
        filters['batch_type'] = batch_type
    if status:
        filters['status'] = status
    if reference:
        filters['reference'] = reference
    return retrieve_batches(db=db, filters=filters)

@router.get("/single/{batch_id}", response_model=BatchResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def get_single(request: Request, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db), batch_id: int = 0):
    return retrieve_single_batch(db=db, id=batch_id)

@router.post("/continue_failed", response_model=PlainResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def continue_failed_batch(request: Request, fields: ContinueBatchModel, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db)):
    req = continue_batch(db=db, batch_id=fields.batch_id)
    return req
