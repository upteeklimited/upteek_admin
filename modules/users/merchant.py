from typing import Dict
from sqlalchemy.orm import Session
from database.model import delete_merchant, get_main_single_merchant_by_id, get_merchants
from fastapi_pagination.ext.sqlalchemy import paginate

def remove_merchant(db: Session, merchant_id: int=0):
	delete_merchant(db=db, id=merchant_id)
	return {
        'status': True,
        'message': 'Success',
    }

def retrieve_merchants(db: Session, filters: Dict={}):
    data = get_merchants(db=db, filters=filters)
    return paginate(data)

def retrieve_single_merchant(db: Session, merchant_id: int=0):
    merchant = get_main_single_merchant_by_id(db=db, id=merchant_id)
    if merchant is None:
        return {
            'status': False,
            'message': 'Merchant not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': merchant
        }
