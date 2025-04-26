from sqlalchemy.orm import Session
from database.model import create_system_configuration, get_single_account_type_by_product_id
from modules.accounting.gls import create_gl

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
    create_system_configuration(db=db, name="merchant_sales_commission_percentage", single_value="0.5")
    create_system_configuration(db=db, name="customer_purchase_commission_percentage", single_value="0.5")
    order_fee_account_code = "41090000"
    order_fee_resp = create_gl(db=db, account_type_code=order_fee_account_code, account_name="Order Fee", 
    created_by=1, authorized_by=1)
    if order_fee_resp['status'] == True:
        order_gl = order_fee_resp['data']
        create_system_configuration(db=db, name="order_fee_account_number", single_value=order_gl.account_number)
    order_suspense_account_code = "70000700"
    order_susp_resp = create_gl(db=db, account_type_code=order_suspense_account_code, account_name="Order Suspense Account", created_by=1, authorized_by=1)
    if order_susp_resp['status'] == True:
        order_susp_gl = order_susp_resp['data']
        create_system_configuration(db=db, name="order_suspense_account_number", single_value=order_susp_gl.account_number)
    return True