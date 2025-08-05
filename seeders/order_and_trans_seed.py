from sqlalchemy.orm import Session
from modules.miscelleanous.ghost import fund_all_seeded_customers, customer_users_random_purchase


def run_fund_seed(db: Session, commit: bool=False):
	print(fund_all_seeded_customers(db=db, amount=100000, commit=commit))
	return True


def run_purchase_seed(db: Session, commit: bool=False):
	print(customer_users_random_purchase(db=db, commit=commit))
	return True
