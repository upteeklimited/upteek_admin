from typing import Dict, List
from database.model import create_user_with_relevant_rows, create_product, get_single_user_by_id, get_single_user_by_email
from modules.utils.tools import generate_slug
from sqlalchemy.orm import Session
from modules.authentication.auth import generate_new_user_account
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(current_dir, "../"))
mock_file_path = os.path.join(base_dir, "templates", "mock_data.json")

def run_mock_seeder(db: Session, commit: bool=False):
    global mock_file_path
    mock_data = None
    with open(mock_file_path, 'r') as file:
        mock_data = json.load(file)
    if mock_data is None:
        return False
    else:
        if len(mock_data) > 0:
            for i in range(len(mock_data)):
                mdata = mock_data[i]
                memail = mdata['merchant_email']
                cuser = get_single_user_by_email(db=db, email=memail)
                if cuser is not None:
                    continue
                else:
                    reguser = create_user_with_relevant_rows(db=db, country_id=1, currency_id=mdata['merchant_currency_id'], username=mdata['merchant_email'], email=mdata['merchant_email'], phone_number=mdata['phone_number'], password="secret", user_type=3, role=1, first_name=mdata['first_name'], other_name=mdata['other_name'], last_name=mdata['last_name'], date_of_birth=mdata['date_of_birth'], gender=mdata['gender'], bio=mdata['bio'], is_merchant=True, merchant_category_id=mdata['merchant_category_id'], merchant_currency_id=mdata['merchant_currency_id'], merchant_name=mdata['merchant_name'], merchant_trading_name=mdata['merchant_trading_name'], merchant_description=mdata['merchant_description'], merchant_email=mdata['merchant_email'], merchant_phone_number=mdata['merchant_phone_number'], commit=commit)
                    user = get_single_user_by_id(db=db, id=reguser.id)
                    acct_name1 = mdata['merchant_name']
                    print(generate_new_user_account(db=db, user_id=user.id, merchant_id=user.merchant_id, account_name=acct_name1, is_merchant=True, commit=commit))
                    merchant_id = user.merchant_id
                    merchant_currency_id = mdata['merchant_currency_id']
                    products = mdata['products']
                    if len(products) > 0:
                        for x in range(len(products)):
                            product = products[x]
                            files_meta_data = []
                            images = product['images']
                            if len(images) > 0:
                                for y in range(len(images)):
                                    files_meta_data.append({
                                        'filename': "file" + str(y),
                                        'url': images[y],
                                        'external_reference': None,
                                        'is_seeded': 0,
                                    })
                            pro_slug = generate_slug(text=product['name'])
                            create_product(db=db, merchant_id=merchant_id, category_id=product['category_id'], currency_id=product['currency_id'], name=product['name'], description=product['description'], product_type=product['product_type'], service_pricing=product['service_pricing'], slug=pro_slug, units=product['units'], weight=product['weight'], cost_price=product['cost_price'], price=product['price'], minimum_price=product['minimum_price'], maximum_price=product['maximum_price'], discount_price=product['discount_price'], discount=product['discount'], discount_type=product['discount_type'], special_note=product['special_note'], unit_low_level=product['unit_low_level'], files_meta_data=files_meta_data, notify_if_available=product['notify_if_available'], condition_status=product['condition_status'], service_delivery_mode=product['service_delivery_mode'], service_is_time_sensitive=product['service_is_time_sensitive'], service_available_days_data=product['service_available_days_data'], service_addon_extra_charge_meta_data=product['service_addon_extra_charge_meta_data'], service_available_time_data=product['service_available_time_data'], status=product['status'], created_by=user.id, commit=commit)
        return True