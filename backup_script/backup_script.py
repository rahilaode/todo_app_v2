import os
import datetime
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST") # Nama service postgresql
DB_PORT = os.getenv("DB_PORT") # Port service postgresql
DB_USER = os.getenv("DB_USER") # User postgresql
DB_PASSWORD = os.getenv("DB_PASSWORD") # Password postgresql
DB_NAME = os.getenv("DB_NAME") # Nama database postgresql
DB_OWNER = os.getenv("DB_OWNER")


BACKUP_DIR = "/backup"

backup_file = os.path.join(BACKUP_DIR,f"bakcup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql")

command = f"pg_dump -h {DB_HOST} -p {DB_PORT} -U {DB_USER} -d {DB_NAME} -F p -f {backup_file} -O -x --role={DB_OWNER}"

os.system(command)