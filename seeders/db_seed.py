from sqlalchemy.orm import Session
from seeders.country_seed import run_country_seeder
from seeders.currency_seed import run_currency_seeder
from seeders.geo_seed import run_geo_seeder
from seeders.category_seed import run_category_seeder, run_product_categories_seeder
from seeders.user_seeder import run_user_seeder
from seeders.sp_seed import seed_services, seed_providers
from seeders.gl_type_seed import seed_gl_type
from seeders.fin_product_seed import seed_financial_products
from seeders.trans_type_seed import seed_trans_type
from seeders.config_seeder import run_config_seeder
from seeders.fin_inst_seed import seed_financial_institutions
import traceback

def run_seed(db: Session):
    try:
        print(run_country_seeder(db=db))
        print(run_currency_seeder(db=db))
        print(run_geo_seeder(db=db))
        print(run_category_seeder(db=db))
        print(run_product_categories_seeder(db=db))
        print(run_user_seeder(db=db))
        print(seed_gl_type(db=db))
        print(seed_financial_products(db=db))
        print(seed_services(db=db))
        print(seed_providers(db=db))
        print(seed_trans_type(db=db))
        print(run_config_seeder(db=db))
        print(seed_financial_institutions(db=db))
        return {
            'status': True,
            'message': 'Seeders ran successfully!'
        }
    except Exception as e:
        err = "Stack Trace - %s \n" % (traceback.format_exc())
        return {
            'status': False,
            'message': err
        }