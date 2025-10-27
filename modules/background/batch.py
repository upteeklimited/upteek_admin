from typing import Dict
from sqlalchemy.orm import Session
from database.model import get_batches, get_single_batch_by_id, update_batch
from fastapi_pagination.ext.sqlalchemy import paginate

def retrieve_batches(db: Session, filters: Dict={}):
	data = get_batches(db=db, filters=filters)
	return paginate(data)

def retrieve_single_batch(db: Session, batch_id: int=0):
	batch = get_single_batch_by_id(db=db, id=batch_id)
	if batch is None:
		return {
		    'status': False,
		    'message': 'Batch not found',
		    'data': None
		}
	else:
		return {
		    'status': True,
		    'message': 'Success',
		    'data': batch
		}

def continue_batch(db: Session, batch_id: int=0):
	batch = get_single_batch_by_id(db=db, id=batch_id)
	if batch is None:
		return {
		    'status': False,
		    'message': 'Batch not found',
		}
	else:
		if batch.status != 2:
			return {
				'status': False,
				'message': 'Batch is not failed',
			}
		else:
			update_batch(db=db, id=batch_id, values={'status': 1})
			return {
				'status': True,
				'message': 'Success',
			}
