from sqlalchemy.orm import Session
from database.model import create_general_ledger_account_type

def seed_gl_type(db: Session):
    seed = [
        {
            'account_code': '10000000',
            'name': 'General Asset',
            'desc': 'General Asset Type',
            'type_num': 1,
        },
        {
            'account_code': '20000000',
            'name': 'General Liability',
            'desc': 'General Liability Type',
            'type_num': 2,
        },
        {
            'account_code': '30000000',
            'name': 'General Equity',
            'desc': 'General Equity Type',
            'type_num': 3,
        },
        {
            'account_code': '40000000',
            'name': 'General Income',
            'desc': 'General Income Type',
            'type_num': 4,
        },
        {
            'account_code': '50000000',
            'name': 'General Expense',
            'desc': 'General Expense Type',
            'type_num': 5,
        },
        {
            'account_code': '70000000',
            'name': 'General Suspense',
            'desc': 'General Suspense Type',
            'type_num': 7,
        },
        {
            'account_code': '10000100',
            'name': 'Loan Account',
            'desc': 'Loan Account Description',
            'type_num': 1,
        },
        {
            'account_code': '10000200',
            'name': 'Fixed Asset',
            'desc': 'Fixed Asset Description',
            'type_num': 1,
        },
        {
            'account_code': '10000300',
            'name': 'Current Asset',
            'desc': 'Current Asset Description',
            'type_num': 1,
        },
        {
            'account_code': '20000100',
            'name': 'Fixed Deposit Account',
            'desc': 'Fixed Deposit Account Description',
            'type_num': 2,
        },
        {
            'account_code': '20000200',
            'name': 'Current Account',
            'desc': 'Current Account Description',
            'type_num': 2,
        },
        {
            'account_code': '20000300',
            'name': 'Savings Account',
            'desc': 'Savings Account Description',
            'type_num': 2,
        },
        {
            'account_code': '20000400',
            'name': 'VAT collections',
            'desc': 'VAT collections Description',
            'type_num': 2,
        },
        {
            'account_code': '20000500',
            'name': 'WHT collections',
            'desc': 'WHT collections Description',
            'type_num': 2,
        },
        {
            'account_code': '40000100',
            'name': 'Loan Internal Accrued',
            'desc': 'Loan Internal Accrued Description',
            'type_num': 4,
        },
        {
            'account_code': '40000200',
            'name': 'Charges On Transactions(C.O.T)',
            'desc': 'Charges On Transactions(C.O.T) Description',
            'type_num': 4,
        },
        {
            'account_code': '40000300',
            'name': 'Forced Liquidation (F.L.D)',
            'desc': 'Forced Liquidation (F.L.D) Description',
            'type_num': 4,
        },
        {
            'account_code': '40000400',
            'name': 'BVN charges',
            'desc': 'BVN charges Description',
            'type_num': 4,
        },
        {
            'account_code': '40000500',
            'name': 'Loan Management Fee',
            'desc': 'Loan Management Fee Description',
            'type_num': 4,
        },
        {
            'account_code': '40000600',
            'name': 'Loan Processing Fee',
            'desc': 'Loan Processing Fee Description',
            'type_num': 4,
        },
        {
            'account_code': '40000700',
            'name': 'SMS Charges',
            'desc': 'SMS Charges Description',
            'type_num': 4,
        },
        {
            'account_code': '40000800',
            'name': 'Card Issue Charges',
            'desc': 'Card Issue Charges Description',
            'type_num': 4,
        },
        {
            'account_code': '40000900',
            'name': 'Interest Received',
            'desc': 'Interest Received Description',
            'type_num': 4,
        },
        {
            'account_code': '40070000',
            'name': 'SMS Income',
            'desc': 'SMS Income Description',
            'type_num': 4,
        },
        {
            'account_code': '40080000',
            'name': 'COT Accrual',
            'desc': 'COT Accrual Description',
            'type_num': 4,
        },
        {
            'account_code': '50000110',
            'name': 'Loan Writen Off',
            'desc': 'Loan Writen Off Description',
            'type_num': 5,
        },
        {
            'account_code': '50000200',
            'name': 'Savings Interest Accrued',
            'desc': 'Savings Interest Accrued Description',
            'type_num': 5,
        },
        {
            'account_code': '50000300',
            'name': 'Provisioned Loans',
            'desc': 'Provisioned Loans Description',
            'type_num': 5,
        },
        {
            'account_code': '70000100',
            'name': 'Inter Branch Suspense Account',
            'desc': 'Inter Branch Suspense Account Description',
            'type_num': 7,
        },
        {
            'account_code': '70000200',
            'name': 'Inter Department Suspense Account',
            'desc': 'Inter Department Suspense Account Description',
            'type_num': 7,
        },
        {
            'account_code': '70000300',
            'name': 'NIBSS TSS Suspense Account',
            'desc': 'NIBSS TSS Suspense Account Description',
            'type_num': 7,
        },
        {
            'account_code': '10123000',
            'name': 'Vault Cash Ledgers',
            'desc': 'Vault Cash Ledgers Description',
            'type_num': 1,
        },
        {
            'account_code': '10000400',
            'name': 'Bills Asset',
            'desc': 'Bills Asset Description',
            'type_num': 1,
        },
        {
            'account_code': '40090000',
            'name': 'NIBSS Fees',
            'desc': 'NIBSS Fees Description',
            'type_num': 4,
        },
        {
            'account_code': '40010001',
            'name': 'Bills Fees',
            'desc': 'Bills Fees Description',
            'type_num': 4,
        },
        {
            'account_code': '70000400',
            'name': 'General Suspense Account',
            'desc': 'General Suspense Account Description',
            'type_num': 7,
        },
        {
            'account_code': '41090000',
            'name': 'General Revenue Account',
            'desc': 'General Revenue Account Description',
            'type_num': 4,
        },
    ]
    if len(seed) > 0:
        for i in range(len(seed)):
            create_general_ledger_account_type(db=db, country_id=1, currency_id=1, name=seed[i]['name'], description=seed[i]['desc'], account_code=seed[i]['account_code'], type_number=seed[i]['type_num'], status=1, created_by=1, authorized_by=1)
    return True
