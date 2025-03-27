from sqlalchemy.orm import Session
from seeders.geo_seed import run_geo_seeder
from seeders.user_seeder import run_user_seeder
from modules.utils.tools import truncate_all_tables

def run_seed(db: Session):
    tru = truncate_all_tables(db=db)
    if tru['status'] == False:
        return tru
    else:
        print(run_geo_seeder(db=db))
        print(run_user_seeder(db=db))
        return {
            'status': True,
            'message': 'Seeders ran successfully!'
        }