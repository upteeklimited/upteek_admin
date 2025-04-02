from typing import Dict
from sqlalchemy.orm import Session
from database.model import update_profile_by_user_id, update_setting_by_user_id
from modules.utils.tools import process_schema_dictionary
