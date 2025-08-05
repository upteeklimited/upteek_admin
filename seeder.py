import sys
sys.path.append("/var/www/adminapi/libs/")
from database.db import session, has_uncommitted_changes
from seeders.db_seed import run_seed

db = session

print(run_seed(db=db, commit=True))
