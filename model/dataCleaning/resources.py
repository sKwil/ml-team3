import os.path

WORKING_DIR = os.getcwd()

DATA_DIR = os.path.join(
    os.path.abspath(os.path.join(WORKING_DIR, os.pardir, os.pardir)),
    'data'
)

SQL_DIR = os.path.join(DATA_DIR, 'sql')

DATABASE = os.path.join(SQL_DIR, 'weather.db')

DATABASE_SETUP_SCRIPT = os.path.join(WORKING_DIR, 'setup.sql')

DATA_RAW_DIR = os.path.join(DATA_DIR, 'raw')

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
