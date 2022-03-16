import os.path

WORKING_DIR = os.getcwd()

DATA_DIR = os.path.join(
    os.path.abspath(os.path.join(WORKING_DIR, os.pardir, os.pardir)),
    'data'
)

SQL_DIR = os.path.join(DATA_DIR, 'sql')

DATABASE = os.path.join(SQL_DIR, 'weather.db')

DATABASE_SETUP_SCRIPT = os.path.join(WORKING_DIR, 'setup.sql')