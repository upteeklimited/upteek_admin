from typing import Dict, List, Any
from sqlalchemy.orm import Session
from database.model import get_orders, get_single_order_by_id
from fastapi_pagination.ext.sqlalchemy import paginate

def retrieve_orders(db: Session, filters: Dict={}):
    data = get_orders(db=db, filters=filters)
    return paginate(data)

def retrieve_single_order(db: Session, id: int=0):
    order = get_single_order_by_id(db=db, id=id)
    if order is None:
        return {
            'status': False,
            'message': 'Order not found',
            'data': None
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': order
        }

def retrieve_order_stats(db: Session):
    total_order = 0
    pending_order = 0
    completed_order = 0
    failed_order = 0
    data = {
        "total_order": total_order,
        "pending_order": pending_order,
        "completed_order": completed_order,
        "failed_order": failed_order,
    }
    return {
        "status": True,
        "message": "Success",
        "data": data
    }