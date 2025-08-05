import sys
sys.path.append("/var/www/adminapi/libs/")
from database.db import session
from seeders.db_seed import run_seed

db = session

print(run_seed(db=db))