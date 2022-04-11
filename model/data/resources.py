import os.path

# Top level project directories
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
MODEL_DIR = os.path.join(PROJECT_ROOT, 'model')

# Database references
DATA_RAW_DIR = os.path.join(DATA_DIR, 'raw')
SQL_DIR = os.path.join(DATA_DIR, 'sql')
DATABASE = os.path.join(SQL_DIR, 'weather.db')

# SQL scripts for data cleaning
SETUP_SQL_DIR = os.path.join(MODEL_DIR, 'data', 'setup', 'sql')
DB_SETUP_SCRIPT = os.path.join(SETUP_SQL_DIR, 'setup.sql')
DB_MONTHS = os.path.join(SETUP_SQL_DIR, 'months.sql')
DB_MERGE_MONTHLY = os.path.join(SETUP_SQL_DIR, 'merge_monthly_data.sql')
DB_CLEAN_DATA_SCRIPT = os.path.join(SETUP_SQL_DIR, 'clean_data.sql')
DB_DAY_PHASE_SCRIPT = os.path.join(SETUP_SQL_DIR, 'day_phase.sql')

# The standard time format for the database
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# The names of all the raw data files. Note that the order here is very
# important, as it corresponds with the Weather table and the
# db.loadWeatherData() method that fills the table.
DATA_FILES = ['temperature.csv',
              'humidity.csv',
              'pressure.csv',
              'weather_description.csv',
              'wind_direction.csv',
              'wind_speed.csv']
