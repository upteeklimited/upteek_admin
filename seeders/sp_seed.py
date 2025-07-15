from sqlalchemy.orm import Session
from database.model import create_provider, check_provider_exist, create_service, check_service_exist, get_last_general_ledger_account, get_single_general_ledger_account_type_by_account_code, create_general_ledger_account
from modules.utils.acct import generate_internal_gl_number

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
		# {
		# 	'name': 'Quickteller',
		# 	'description': 'Quickteller',
		# 	'code': 'quickteller',
		# 	'status': 1,
		# },
		# {
		# 	'name': 'Paystack',
		# 	'description': 'Paystack',
		# 	'code': 'paystack',
		# 	'status': 1,
		# },
		# {
		# 	'name': 'Flutterwave',
		# 	'description': 'Flutterwave',
		# 	'code': 'flutterwave',
		# 	'status': 1,
		# },
		# {
		# 	'name': 'BankOne',
		# 	'description': 'BankOne',
		# 	'code': 'bankone',
		# 	'status': 1,
		# },
		# {
		# 	'name': 'SmileID',
		# 	'description': 'SmileID',
		# 	'code': 'smileid',
		# 	'status': 1,
		# },
		# {
		# 	'name': 'SquadCo',
		# 	'description': 'SquadCo',
		# 	'code': 'squadco',
		# 	'status': 1,
		# },
		{
			'name': 'Fincra',
			'description': 'Fincra',
			'code': 'fincra',
			'status': 1,
		},
	]
	last_gl_id = 0
	last_gl = get_last_general_ledger_account(db=db)
	if last_gl is not None:
		last_gl_id = last_gl.id
	liability_account_code = "20000000"
	liability_type_id = 0
	liability_type = get_single_general_ledger_account_type_by_account_code(db=db, account_code=liability_account_code)
	if liability_type is not None:
		liability_type_id = liability_type.id
	if len(data) > 0:
		for i in range(len(data)):
			if check_provider_exist(db=db, code=data[i]['code']) == False:
				provider_account_name = data[i]['name'] + " Provider Account"
				gl_account = create_general_ledger_account(db=db, type_id=liability_type_id, name=provider_account_name, account_number=generate_internal_gl_number(type_code=liability_account_code, last_id=last_gl_id), created_by=1, authorized_by=1)
				create_provider(db=db, gl_account_id=gl_account.id, name=data[i]['name'], code=data[i]['code'], status=data[i]['status'])
				last_gl_id = gl_account.id
	return True