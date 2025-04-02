from typing import Dict
from sqlalchemy.orm import Session
from database.model import update_profile_by_user_id, update_setting_by_user_id
from modules.utils.tools import process_schema_dictionary


def update_user_profile_details(db: Session, user_id: int=0, values: Dict={}):
    passvalues = process_schema_dictionary(info=values)
    update_profile_by_user_id(db=db, user_id=user_id, values=passvalues)
    return {
        'status': True,
        'message': 'Success'
    }

# def update_user