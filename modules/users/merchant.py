from typing import Dict
from fastapi import UploadFile
from sqlalchemy.orm import Session
from database.model import create_merchant, update_merchant, delete_merchant, get_single_merchant_info_by_id, get_merchants, create_merchant_user, update_merchant_user, force_delete_merchant_user, check_user_id_merchant_id, get_single_merchant_user_by_user_id_merchant_id
from modules.utils.tools import process_schema_dictionary, generate_slug
from modules.utils.files import upload_request_file_to_cloudinary
from modules.authentication.auth import generate_new_user_account
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
    merchant = get_single_merchant_info_by_id(db=db, id=merchant_id)
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
