from sqlalchemy.orm import Session
from database.model import create_provider, check_provider_exist, create_service, check_service_exist

def seed_services(db: Session):
	data = [
		{
			'name': 'Nigerian Bank Transfer Name Validation',
			'description': 'Nigerian Bank Transfer Name Validation',
			'code': 'nigerian_bank_name_validation',
			'status': 1,
		},
		{
			'name': 'Nigerian Bank Transfer',
			'description': 'Nigerian Bank Transfer',
			'code': 'nigerian_bank_transfer',
			'status': 1,
		},
		{
			'name': 'Nigerian Airtime Service',
			'description': 'Nigerian Airtime Service',
			'code': 'nigerian_airtime_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Data Service',
			'description': 'Nigerian Data Service',
			'code': 'nigerian_data_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Internet Service',
			'description': 'Nigerian Internet Service',
			'code': 'nigerian_internet_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Utility Bill Service',
			'description': 'Nigerian Utility Bill Service',
			'code': 'nigerian_utility_bill_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Cable Service',
			'description': 'Nigerian Cable Service',
			'code': 'nigerian_cable_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Betting Service',
			'description': 'Nigerian Betting Service',
			'code': 'nigerian_betting_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Government Bill Service',
			'description': 'Nigerian Government Bill Service',
			'code': 'nigerian_government_bill_service',
			'status': 1,
		},
		{
			'name': 'Nigerian Toll Bill Service',
			'description': 'Nigerian Toll Bill Service',
			'code': 'nigerian_toll_service',
			'status': 1,
		},
	]
	print(data)
	if len(data) > 0:
		for i in range(len(data)):
			if check_service_exist(db=db, code=data[i]['code']) == 0:
				create_service(db=db, name=data[i]['name'], code=data[i]['code'], status=data[i]['status'])
	return True

def seed_providers(db: Session):
	data = [
		{
			'name': 'Quickteller',
			'description': 'Quickteller',
			'code': 'quickteller',
			'status': 1,
		},
		{
			'name': 'Paystack',
			'description': 'Paystack',
			'code': 'paystack',
			'status': 1,
		},
		{
			'name': 'Flutterwave',
			'description': 'Flutterwave',
			'code': 'flutterwave',
			'status': 1,
		},
		{
			'name': 'BankOne',
			'description': 'BankOne',
			'code': 'bankone',
			'status': 1,
		},
	]
	if len(data) > 0:
		for i in range(len(data)):
			if check_provider_exist(db=db, code=data[i]['code']) == False:
				create_provider(db=db, name=data[i]['name'], code=data[i]['code'], status=data[i]['status'])
	return True