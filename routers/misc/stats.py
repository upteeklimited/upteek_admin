from fastapi import APIRouter, Request, Depends, Query
from modules.miscelleanous.statistics import get_main_statistics, get_user_registration_stats, get_revenue_report_stats
from database.schema import ErrorResponse, MainStatsResponseModel, UserRegStatResponseModel, RevenueReportStatsResponse
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi_pagination import Page

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"]
)

@router.get("/", response_model=MainStatsResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def stats(request: Request, db: Session = Depends(get_session)):
    return get_main_statistics(db=db)


@router.get("/user_statistics", response_model=UserRegStatResponseModel, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def user_stats(request: Request, db: Session = Depends(get_session), timeline: str = Query(None), days: int = Query(None)):
    return get_user_registration_stats(db=db, timeline=timeline, days=days)

@router.get("/revenue_report_graph", response_model=RevenueReportStatsResponse, responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}})
async def revenue_report_graph(request: Request, db: Session = Depends(get_session), timeline: str = Query(None), value_range: int = Query(None)):
    return get_revenue_report_stats(db=db, timeline=timeline, value_range=value_range)
