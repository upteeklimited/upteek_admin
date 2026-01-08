from typing import Dict
from sqlalchemy.orm import Session
from database.model import sum_of_transactions, get_ids_of_general_ledger_account_types, get_ids_of_general_ledger_accounts
from fastapi_pagination.ext.sqlalchemy import paginate


def get_revenue_between_dates(db: Session, from_date: str=None, to_date: str=None):
	gl_type_ids = get_ids_of_general_ledger_account_types(db=db, filters={'type_number': 4})
	gl_ids = get_ids_of_general_ledger_accounts(db=db, filters={'type_ids': gl_type_ids})
	revenue_amount = sum_of_transactions(db=db, filters={'gl_ids': gl_ids, 'from_date': from_date, 'to_date': to_date})
	return {
		"status": True,
		"message": "Success",
		"data": float(revenue_amount),
	}

def get_expense_between_dates(db: Session, from_date: str=None, to_date: str=None):
	gl_type_ids = get_ids_of_general_ledger_account_types(db=db, filters={'type_number': 5})
	gl_ids = get_ids_of_general_ledger_accounts(db=db, filters={'type_ids': gl_type_ids})
	expense_amount = sum_of_transactions(db=db, filters={'gl_ids': gl_ids, 'from_date': from_date, 'to_date': to_date})
	return {
		"status": True,
		"message": "Success",
		"data": float(expense_amount),
	}

