from sqlalchemy.orm import Session
from database.model import create_system_configuration, get_single_account_type_by_product_id
from modules.accounting.gls import create_gl
import json

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
    vat_account_code = "20000000"
    vat_resp = create_gl(db=db, account_type_code=vat_account_code, account_name="VAT Account", created_by=1, authorized_by=1)
    if vat_resp['status'] == True:
        vat_resp_gl = vat_resp['data']
        create_system_configuration(db=db, name="vat_account_number", single_value=vat_resp_gl.account_number)
    wht_account_code = "20000000"
    wht_resp = create_gl(db=db, account_type_code=wht_account_code, account_name="WHT Account", created_by=1, authorized_by=1)
    if wht_resp['status'] == True:
        wht_resp_gl = wht_resp['data']
        create_system_configuration(db=db, name="wht_account_number", single_value=wht_resp_gl.account_number)
    create_system_configuration(db=db, name="default_transfer_provider", single_value="squadco")
    create_system_configuration(db=db, name="allow_internal_transfer", single_value="1")
    create_system_configuration(db=db, name="allow_external_transfer", single_value="1")
    create_system_configuration(db=db, name="collect_internal_transfer_fees", single_value="1")
    create_system_configuration(db=db, name="collect_external_transfer_fees", single_value="1")
    internal_trans_fees = [
        {
            "from": 0,
            "to": 500000,
            "amount": 10,
        },
        {
            "from": 500000,
            "to": 500000000000,
            "amount": 20,
        },
    ]
    create_system_configuration(db=db, name="internal_transfer_fees", multi_value=json.dumps(internal_trans_fees))
    external_trans_fees = [
        {
            "from": 0,
            "to": 500000,
            "amount": 25,
        },
        {
            "from": 500000,
            "to": 500000000000,
            "amount": 50,
        },
    ]
    create_system_configuration(db=db, name="external_transfer_fees", multi_value=json.dumps(external_trans_fees))
    susp_account_code = "70000300"
    susp_resp = create_gl(db=db, account_type_code=susp_account_code, account_name="External Transfer Suspense Account", created_by=1, authorized_by=1)
    if susp_resp['status'] == True:
        susp_resp_gl = susp_resp['data']
        create_system_configuration(db=db, name="external_transfer_suspense_account", single_value=susp_resp_gl.account_number)
    revenue_account_code = "41090000"
    internal_rev_resp = create_gl(db=db, account_type_code=revenue_account_code, account_name="Internal Revenue Account", created_by=1, authorized_by=1)
    if internal_rev_resp['status'] == True:
        internal_rev_resp_gl = internal_rev_resp['data']
        create_system_configuration(db=db, name="internal_transfer_revenue_gl", single_value=internal_rev_resp_gl.account_number)
    external_rev_resp = create_gl(db=db, account_type_code=revenue_account_code, account_name="External Revenue Account", created_by=1, authorized_by=1)
    if external_rev_resp['status'] == True:
        external_rev_resp_gl = external_rev_resp['data']
        create_system_configuration(db=db, name="external_transfer_revenue_gl", single_value=external_rev_resp_gl.account_number)
    create_system_configuration(db=db, name="external_transfer_provider_code", single_value="fincra")
    create_system_configuration(db=db, name="external_transfer_fee_type", single_value="2")
    liability_account_code = "20000000"
    general_deposit_resp = create_gl(db=db, account_type_code=revenue_account_code, account_name="General Deposit Account", created_by=1, authorized_by=1)
    if general_deposit_resp['status'] == True:
        general_deposit_resp_gl = general_deposit_resp['data']
        create_system_configuration(db=db, name="general_deposit_gl", single_value=general_deposit_resp_gl.account_number)
    return True