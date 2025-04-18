from sqlalchemy.orm import Session
from database.model import create_system_configuration, get_single_account_type_by_product_id

def run_config_seeder(db: Session):
    #account type seed
    account_code = ""
    account_type = get_single_account_type_by_product_id(db=db, product_id=1)
    if account_type is not None:
        account_code = account_type.account_code
    create_system_configuration(db=db, name="default_savings_account_code", single_value=account_code)
    return True