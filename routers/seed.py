from fastapi import APIRouter, Request, Depends, HTTPException
from seeders.db_seed import run_seed
from modules.utils.tools import recreate_db
from database.db import get_session
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/seed",
    tags=["Seed"]
)

@router.get("/run")
async def run(request: Request, db: Session = Depends(get_session)):
    return run_seed(db=db)

@router.get("/recreate_database")
async def recreate_database(request: Request, db: Session = Depends(get_session)):
    return recreate_db(db=db)
