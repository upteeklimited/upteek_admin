from typing import Dict
import dateparser
from sqlalchemy.orm import Session
from database.model import get_single_account_by_account_number, get_single_general_ledger_account_by_account_number, get_single_transaction_by_id, get_transactions, search_accounts, search_general_ledger_accounts
from modules.utils.acct import get_gl_ids_by_filters, get_account_ids_by_filters
from fastapi_pagination.ext.sqlalchemy import paginate

def retrieve_accounts(db: Session, search: str=None):
    resp = []
    if search is not None:
        accounts = search_accounts(db=db, search=search)
        if len(accounts) > 0:
            for account in accounts:
                resp.append({
                    'id': account.id,
                    'account_name': account.account_name,
                    'account_number': account.account_number,
                    'nuban': account.nuban,
                    'balance': account.available_balance,
                    'is_gl': False
                })
        gls = search_general_ledger_accounts(db=db, search=search)
        if len(gls) > 0:
            for gl in gls:
                resp.append({
                    'id': gl.id,
                    'account_name': gl.name,
                    'account_number': gl.account_number,
                    'nuban': None,
                    'balance': gl.balance,
                    'is_gl': True
                })
    return resp

def retrieve_transactions(db: Session, filters: Dict={}):
    if 'account_number' in filters:
        gl = get_single_general_ledger_account_by_account_number(db=db, account_number=filters['account_number'])
        if gl is not None:
            filters['gl_id'] = gl.id
        account = get_single_account_by_account_number(db=db, account_number=filters['account_number'])
        if account is not None:
            filters['account_id'] = account.id
        if 'gl_id' not in filters and 'account_id' not in filters:
            filters['account_id'] = 999999999
            filters['gl_id'] = 999999999
    if 'account_name' in filters:
        gls = get_gl_ids_by_filters(db=db, filters={'name': filters['account_name']})
        if len(gls) > 0:
            filters['gl_ids'] = gls
        accounts = get_account_ids_by_filters(db=db, filters={'account_name': filters['account_name']})
        if len(accounts) > 0:
            filters['account_ids'] = accounts
        if 'gl_ids' not in filters and 'account_ids' not in filters:
            filters['account_ids'] = [999999999]
            filters['gl_ids'] = [999999999]
    if 'from_date' in filters:
        if filters['from_date'] is not None:
            filters['from_date'] = dateparser.parse(filters['from_date'])
    if 'to_date' in filters:
        if filters['to_date'] is not None:
            filters['to_date'] = dateparser.parse(filters['to_date'])
    data = get_transactions(db=db, filters=filters)
    return paginate(data)

def retrieve_transaction_by_id(db: Session, transaction_id: int=0):
    trans = get_single_transaction_by_id(db=db, id=transaction_id)
    if trans is None:
        return {
            'status': False,
            'message': 'Transaction not found',
            'data': None,
        }
    else:
        return {
            'status': True,
            'message': 'Success',
            'data': trans,
        }
    