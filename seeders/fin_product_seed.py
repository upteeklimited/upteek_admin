from sqlalchemy.orm import Session
from modules.accounting.gls import create_new_product
from settings.constants import FINANCIAL_PRODUCT_TYPES

def seed_financial_products(db: Session, commit: bool=False):
    seed = [
        {
            'name': 'Customer Savings Account',
            'description': 'Customer Savings Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['savings']['num'],
        },
        {
            'name': 'Merchant Savings Account',
            'description': 'Merchant Savings Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['savings']['num'],
        },
        {
            'name': 'Customer Current Account',
            'description': 'Customer Current Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['current']['num'],
        },
        {
            'name': 'Merchant Current Account',
            'description': 'Merchant Current Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['current']['num'],
        },
        {
            'name': 'Customer Deposit Account',
            'description': 'Customer Deposit Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['deposit']['num'],
        },
        {
            'name': 'Merchant Deposit Account',
            'description': 'Merchant Deposit Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['deposit']['num'],
        },
        {
            'name': 'Customer Loan Account',
            'description': 'Customer Loan Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['loan']['num'],
        },
        {
            'name': 'Merchant Loan Account',
            'description': 'Merchant Loan Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['loan']['num'],
        },
    ]
    if len(seed) > 0:
        for i in range(len(seed)):
            create_new_product(db=db, name=seed[i]['name'], description=seed[i]['description'], product_type=seed[i]['product_type'], created_by=1, authorized_by=1, commit=commit)
    return True