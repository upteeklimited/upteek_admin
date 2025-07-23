from sqlalchemy.orm import Session
from modules.miscelleanous.ghost import fund_all_seeded_customers, customer_users_random_purchase


def run_fund_seed(db: Session):
	print(fund_all_seeded_customers(db=db, amount=100000))
	return True


def run_purchase_seed(db: Session):
	print(customer_users_random_purchase(db=db))
	return True
