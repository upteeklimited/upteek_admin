from sqlalchemy.orm import Session
from database.model import create_transaction_type

def seed_trans_type(db: Session):
    seed = [
        {
            'type_code': '001',
            'type_action': 1,
            'name': 'Debit General',
            'desc': 'Debit General Description',
        },
        {
            'type_code': '002',
            'type_action': 2,
            'name': 'Credit General',
            'desc': 'Credit General Description',
        },
        {
            'type_code': '003',
            'type_action': 1,
            'name': 'Cash Deposit',
            'desc': 'Cash Deposit Description',
        },
        {
            'type_code': '004',
            'type_action': 2,
            'name': 'Cash Withdrawal',
            'desc': 'Cash Withdrawal Description',
        },
        {
            'type_code': '005',
            'type_action': 1,
            'name': 'Cheque Payment',
            'desc': 'Cheque Payment Description',
        },
        {
            'type_code': '006',
            'type_action': 2,
            'name': 'Cheque Deposit',
            'desc': 'Cheque Deposit Description',
        },
        {
            'type_code': '007',
            'type_action': 1,
            'name': 'System Debit',
            'desc': 'System Debit Description',
        },
        {
            'type_code': '008',
            'type_action': 2,
            'name': 'System Credit',
            'desc': 'System Credit Description',
        },
        {
            'type_code': '009',
            'type_action': 2,
            'name': 'Loan Availment Credit',
            'desc': 'Loan Availment Credit Description',
        },
        {
            'type_code': '010',
            'type_action': 1,
            'name': 'Loan Availment Debit',
            'desc': 'Loan Availment Debit Description',
        },
        {
            'type_code': '011',
            'type_action': 2,
            'name': 'Deposit Creation Credit',
            'desc': 'Deposit Creation Credit Description',
        },
        {
            'type_code': '012',
            'type_action': 1,
            'name': 'Deposit Liquidation Debit',
            'desc': 'Deposit Liquidation Debit Description',
        },
        {
            'type_code': '013',
            'type_action': 2,
            'name': 'Forced Liquidation Credit',
            'desc': 'Forced Liquidation Credit Description',
        },
        {
            'type_code': '014',
            'type_action': 1,
            'name': 'Forced Liquidation Debit',
            'desc': 'Forced Liquidation Debit Description',
        },
        {
            'type_code': '015',
            'type_action': 1,
            'name': 'From External Debit',
            'desc': 'External Debit Description',
        },
        {
            'type_code': '016',
            'type_action': 2,
            'name': 'From External Credit',
            'desc': 'External Credit Description',
        },
        {
            'type_code': '017',
            'type_action': 1,
            'name': 'To External Debit',
            'desc': 'External Debit Description',
        },
        {
            'type_code': '018',
            'type_action': 2,
            'name': 'To External Credit',
            'desc': 'External Credit Description',
        },
        {
            'type_code': '019',
            'type_action': 1,
            'name': 'Collection',
            'desc': 'Collection Description',
        },
        {
            'type_code': '020',
            'type_action': 1,
            'name': 'App Debit',
            'desc': 'App Debit Description',
        },
        {
            'type_code': '021',
            'type_action': 2,
            'name': 'App Credit',
            'desc': 'App Credit Description',
        },
        {
            'type_code': '022',
            'type_action': 1,
            'name': 'USSD Debit',
            'desc': 'USSD Debit Description',
        },
        {
            'type_code': '023',
            'type_action': 2,
            'name': 'USSD Credit',
            'desc': 'USSD Credit Description',
        },
        
        {
            'type_code': '024',
            'type_action': 1,
            'name': 'Debit *',
            'desc': 'Old Debit Description',
        },
        {
            'type_code': '025',
            'type_action': 2,
            'name': 'Credit *',
            'desc': 'Old Credit Description',
        },
        {
            'type_code': '026',
            'type_action': 1,
            'name': 'Credit Reversal',
            'desc': 'Credit Reversal Description',
        },
        {
            'type_code': '027',
            'type_action': 2,
            'name': 'Debit Reversal',
            'desc': 'Debit Reversal Description',
        },
        {
            'type_code': '028',
            'type_action': 1,
            'name': 'Approved Overdrafts',
            'desc': 'Approved Overdrafts Description',
        },
        {
            'type_code': '029',
            'type_action': 1,
            'name': 'Order Debit',
            'desc': 'Order Debit Description',
        },
        {
            'type_code': '030',
            'type_action': 2,
            'name': 'Order Credit',
            'desc': 'Order Credit Description',
        },
        {
            'type_code': '031',
            'type_action': 2,
            'name': 'Order Fee',
            'desc': 'Order Fee Description',
        },
        {
            'type_code': '032',
            'type_action': 2,
            'name': 'Loan Payment Credit',
            'desc': 'Loan Payment Credit Description',
        },
        {
            'type_code': '033',
            'type_action': 1,
            'name': 'Loan Payment Debit',
            'desc': 'Loan Payment Debit Description',
        },
    ]
    if len(seed) > 0:
        for i in range(len(seed)):
            create_transaction_type(db=db, code=seed[i]['type_code'], action=seed[i]['type_action'], name=seed[i]['name'], description=seed[i]['desc'], created_by=1, authorized_by=1)
    return True

