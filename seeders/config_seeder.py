from sqlalchemy.orm import Session
from database.model import create_system_configuration, get_single_account_type_by_product_id

def run_config_seeder(db: Session):
    customer_savings_account_code = ""
    customer_savings_account_type = get_single_account_type_by_product_id(db=db, product_id=1)
    if customer_savings_account_type is not None:
        customer_savings_account_code = customer_savings_account_type.account_code
    create_system_configuration(db=db, name="customer_default_savings_account_code", single_value=customer_savings_account_code)
    merchant_savings_account_code = ""
    merchant_savings_account_type = get_single_account_type_by_product_id(db=db, product_id=1)
    if merchant_savings_account_type is not None:
        merchant_savings_account_code = merchant_savings_account_type.account_code
    create_system_configuration(db=db, name="merchant_default_savings_account_code", single_value=merchant_savings_account_code)
    return True