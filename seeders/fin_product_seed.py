from sqlalchemy.orm import Session
from modules.accounting.gls import create_new_product
from settings.constants import FINANCIAL_PRODUCT_TYPES

def seed_financial_products(db: Session):
    seed = [
        {
            'name': 'Savings Account',
            'description': 'Savings Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['savings']['num'],
        },
        {
            'name': 'Current Account',
            'description': 'Current Account Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['current']['num'],
        },
        {
            'name': 'Deposit',
            'description': 'Deposit Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['deposit']['num'],
        },
        {
            'name': 'Loan',
            'description': 'Loan Product',
            'product_type': FINANCIAL_PRODUCT_TYPES['loan']['num'],
        },
    ]
    if len(seed) > 0:
        for i in range(len(seed)):
            create_new_product(db=db, name=seed[i]['name'], description=seed[i]['description'], product_type=seed[i]['product_type'], created_by=1, authorized_by=1)
    return True