from sqlalchemy.orm import Session
from database.model import create_bill_category, create_bill, get_single_provider_by_code, get_single_bill_category_by_code, check_bill_category_exist, check_if_bill_exists, get_single_service_by_code
import json

def seed_bill_categories(db: Session, commit: bool=False):
	data = [
		{
			'country_id': 1,
			'name': 'Airtime',
			'description': 'Nigerian Airtime Category',
			'code': 'ng_airtime',
			'status': 1,
		},
		{
			'country_id': 1,
			'name': 'Data',
			'description': 'Nigerian Data Category',
			'code': 'ng_data',
			'status': 1,
		},
		{
			'country_id': 1,
			'name': 'Internet',
			'description': 'Nigerian Internet Category',
			'code': 'ng_internet',
			'status': 0,
		},
		{
			'country_id': 1,
			'name': 'Utility Bills',
			'description': 'Nigerian Utility Bill Category',
			'code': 'ng_utility',
			'status': 0,
		},
		{
			'country_id': 1,
			'name': 'Cable',
			'description': 'Nigerian Cable Category',
			'code': 'ng_cable',
			'status': 0,
		},
		{
			'country_id': 1,
			'name': ' Betting',
			'description': 'Nigerian Betting Category',
			'code': 'ng_betting',
			'status': 0,
		},
		{
			'country_id': 1,
			'name': 'Nigerian Government',
			'description': 'Nigerian Government Category',
			'code': 'ng_govt',
			'status': 0,
		},
		{
			'country_id': 1,
			'name': 'Toll Services',
			'description': 'Nigerian Toll Category',
			'code': 'ng_toll',
			'status': 0,
		},
	]
	print(data)
	if len(data) > 0:
		for i in range(len(data)):
			if check_bill_category_exist(db=db, code=data[i]['code']) == False:
				create_bill_category(db=db, country_id=data[i]['country_id'], name=data[i]['name'], description=data[i]['description'], code=data[i]['code'], status=data[i]['status'], commit=commit)
	return True


def seed_bills(db: Session, commit: bool=False):
	data = [
		{
			'category': 'ng_airtime',
			'service': 'nigerian_airtime_service',
			'provider': 'squadco',
			'name': 'MTN Airtime',
			'description': 'MTN Airtime',
			'short_name': 'MTN',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_mtn_airtime',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 1,
			'is_data': 0,
			'is_flat': 0,
			'meta_data': {},
		},
		{
			'category': 'ng_airtime',
			'service': 'nigerian_airtime_service',
			'provider': 'squadco',
			'name': 'Airtel Airtime',
			'description': 'Airtel Airtime',
			'short_name': 'Airtel',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_airtel_airtime',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 1,
			'is_data': 0,
			'is_flat': 0,
			'meta_data': {},
		},
		{
			'category': 'ng_airtime',
			'service': 'nigerian_airtime_service',
			'provider': 'squadco',
			'name': 'Glo Airtime',
			'description': 'Glo Airtime',
			'short_name': 'Glo',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_glo_airtime',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 1,
			'is_data': 0,
			'is_flat': 0,
			'meta_data': {},
		},
		{
			'category': 'ng_airtime',
			'service': 'nigerian_airtime_service',
			'provider': 'squadco',
			'name': '9mobile Airtime',
			'description': '9mobile Airtime',
			'short_name': '9mobile',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_9mobile_airtime',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 1,
			'is_data': 0,
			'is_flat': 0,
			'meta_data': {},
		},
		{
			'category': 'ng_data',
			'service': 'nigerian_data_service',
			'provider': 'squadco',
			'name': 'MTN Data',
			'description': 'MTN Data',
			'short_name': 'MTN Data',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_mtn_data',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 0,
			'is_data': 1,
			'is_flat': 0,
			'meta_data': {
				'squadco': {
					'biller_name': 'MTN',
				},
			},
		},
		{
			'category': 'ng_data',
			'service': 'nigerian_data_service',
			'provider': 'squadco',
			'name': 'Airtel Data',
			'description': 'Airtel Data',
			'short_name': 'Airtel Data',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_airtel_data',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 0,
			'is_data': 1,
			'is_flat': 0,
			'meta_data': {
				'squadco': {
					'biller_name': 'Airtel',
				},
			},
		},
		{
			'category': 'ng_data',
			'service': 'nigerian_data_service',
			'provider': 'squadco',
			'name': 'Glo Data',
			'description': 'Glo Data',
			'short_name': 'Glo Data',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_glo_data',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 0,
			'is_data': 1,
			'is_flat': 0,
			'meta_data': {
				'squadco': {
					'biller_name': 'GLO',
				},
			},
		},
		{
			'category': 'ng_data',
			'service': 'nigerian_data_service',
			'provider': 'squadco',
			'name': '9mobile Data',
			'description': '9mobile Data',
			'short_name': '9mobile Data',
			'label_name': 'Mobile Number',
			'code': 'bp_ng_9mobile_data',
			'amount': 0,
			'minimum_amount': 50,
			'maximum_amount': 10000000,
			'fee': 0,
			'commission': 0.02,
			'is_airtime': 0,
			'is_data': 1,
			'is_flat': 0,
			'meta_data': {
				'squadco': {
					'biller_name': '9mobile',
				},
			},
		},
	]
	print(data)
	if len(data) > 0:
		for i in range(len(data)):
			category_id = 0
			category = get_single_bill_category_by_code(db=db, code=data[i]['category'])
			if category is not None:
				category_id = category.id
			service_id = 0
			service = get_single_service_by_code(db=db, code=data[i]['service'])
			if service is not None:
				service_id = service.id
			provider_id = 0
			provider = get_single_provider_by_code(db=db, code=data[i]['provider'])
			if provider is not None:
				provider_id = provider.id
			create_bill(db=db, country_id=1, currency_id=1, category_id=category_id, service_id=service_id, provider_id=provider_id, name=data[i]['name'], description=data[i]['description'], short_name=data[i]['short_name'], label=data[i]['label_name'], code=data[i]['code'], amount=data[i]['amount'], minimum_amount=data[i]['minimum_amount'], maximum_amount=data[i]['maximum_amount'], fee=data[i]['fee'], commission=data[i]['commission'], is_airtime=data[i]['is_airtime'], is_data=data[i]['is_data'], is_flat=data[i]['is_flat'], meta_data=json.dumps(data[i]['meta_data']), status=1, commit=commit)
	True