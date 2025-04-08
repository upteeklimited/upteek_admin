from sqlalchemy.orm import Session
from seeders.country_seed import run_country_seeder
from seeders.currency_seed import run_currency_seeder
from seeders.geo_seed import run_geo_seeder
from seeders.category_seed import run_category_seeder
from seeders.user_seeder import run_user_seeder
import traceback

def run_seed(db: Session):
    try:
        print(run_country_seeder(db=db))
        print(run_currency_seeder(db=db))
        print(run_geo_seeder(db=db))
        print(run_category_seeder(db=db))
        print(run_user_seeder(db=db))
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