import csv
import os

from tqdm import tqdm

import model.data.resources as re
from model.data import db
from model.data.load import loader
from model.data.setup import sql_strings as sql
from model.data.setup import util as ut
from model.data import data_files as df


def install():
    """
    Run each of the setup methods within this file, thereby deleting the
    existing sqlite database and then recreating it from the raw data. The
    setup is performed in this order:

    1. The existing database is cleared, dropping all the tables.
    2. The database is recreated and configured with two tables called
       Cities and Weather
    3. Import the city data into the database
    4. Import the weather data into the database
    5. Create SQL views to filter the dat
    """

    print('Deleting existing database...')
    try:
        delete_db()
    except OSError:
        print('Installation failed.')
        print('  The database file may be in use by another program.')
        return

    print('Configuring weather database...')
    ut.run_script(re.DB_SETUP_SCRIPT)

    print('Loading Weather Stations...')
    load_stations()
    print('  Added', loader.get_stations_rows(), 'stations to SQL database')

    print('Loading Precipitation Data...')
    load_precipitation_data()

    """
    print('Loading Weather data...')
    load_weather_data()
    print('  Successfully loaded', loader.get_weather_rows(), 'weather rows')

    print('Creating DayPhase table...')
    ut.run_script(re.DB_DAY_PHASE_SCRIPT)

    print('Creating WeatherDesc table...')
    ut.run_script(re.DB_WEATHER_DESC_SCRIPT)

    print('Cleaning weather data...')
    ut.run_script(re.DB_CLEAN_DATA_SCRIPT)

    print('Creating SQL views...')
    ut.run_script(re.DB_CREATE_VIEWS_SCRIPT)
    """

    print('Finished SQLite installation')


def delete_db():
    """
    Delete the sqlite database file, if it exists. If it does not exist,
    nothing happens.

    If the file is currently in use, an exception will be thrown which must
    be caught.
    """

    if os.path.exists(re.DATABASE):
        os.remove(re.DATABASE)


def load_stations():
    """
    Load the cities from the city_attributes.csv file and put them in the
    Cities table.

    Warning: This overwrites any existing data by first clearing the Cities
    table.
    """

    # Open a connection to the sqlite database
    with db.get_conn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_STATIONS_TABLE)

        with open(df.ALL_STATIONS) as file:
            rows = ut.get_data_file_lines(df.ALL_STATIONS)
            progress_bar = tqdm(total=rows, desc='Reading stations...')

            # Read the data one row at a time, sending it to the database
            for row in file:
                # The substring character ranges here come from the readme.txt
                station_id = row[0:11].strip()
                latitude = float(row[12:20])
                longitude = float(row[21:30])
                elevation = float(row[31:37])
                state = row[38:40]
                name = row[41:71].strip()
                gsn_flag = row[72:75].strip()
                hcn_flag = row[76:79].strip()
                wmo_id = row[80:85].strip()

                conn.execute(sql.ADD_STATION,
                             (station_id, latitude, longitude, elevation,
                              state, name, gsn_flag, hcn_flag, wmo_id))
                progress_bar.update(1)

            progress_bar.close()


def load_precipitation_data():
    """
    Load all the weather data from products/precipitation/* files.
    """

    # List the data files and their corresponding SQL statements (and the
    # multiplying factor for correcting the units)
    files = [
        ('mly-prcp-50pctl.txt', sql.ADD_PRECIPITATION_MEDIAN, 0.01),
        ('mly-prcp-avgnds-ge001hi.txt', sql.ADD_PRECIPITATION_DAYS_H, 1),
        ('mly-prcp-avgnds-ge010hi.txt', sql.ADD_PRECIPITATION_DAYS_T, 1),
        ('mly-prcp-normal.txt', sql.ADD_PRECIPITATION_NORMALS, 0.01),
        ('mly-snow-50pctl.txt', sql.ADD_SNOWFALL_MEDIAN, 0.1),
        ('mly-snow-avgnds-ge001ti.txt', sql.ADD_SNOWFALL_DAYS_T, 1),
        ('mly-snow-avgnds-ge010ti.txt', sql.ADD_SNOWFALL_DAYS_I, 1),
        ('mly-snow-normal.txt', sql.ADD_SNOWFALL_NORMALS, 0.1),
        ('mly-snwd-avgnds-ge001wi.txt', sql.ADD_SNOW_DEPTH_DAYS, 1)
    ]

    # Total iterations is the total number of lines in every file, times 12
    # (for each month)
    total_iterations = sum([
        ut.get_data_file_lines(os.path.join(df.__PRECIPITATION_DIR, f)) for
        f, s, u in files
    ]) * 12

    progress_bar = tqdm(total=total_iterations,
                        desc='Reading precipitation data...')

    # Connect to the SQLite database
    with db.get_conn() as conn:
        # Iterate for each data file in the precipitation folder
        for file_name, sql_script, factor in files:
            # Open the file
            with open(os.path.join(df.__PRECIPITATION_DIR, file_name)) as file:
                # Process each row in the file
                for row in file:
                    # Get the station id, and process the data for each month
                    station_id = row[0:11].strip()
                    for i in range(1, 13):
                        progress_bar.update(1)
                        value = float(row[11 + 7 * i:16 + 7 * i]) * factor
                        flag = row[16 + 7 * i].strip()
                        conn.execute(sql_script, (station_id, i, value, flag))


def load_weather_data():
    """
    Load all the weather data for each city from the csv files. Send this
    data to the sqlite database in the Weather table.

    Warning: This overwrites any existing data by first clearing the Weather
    table.

    The goal of this method is to take data in this format (in this case for
    temperature):
    +---------------------+-----------+----------+---------------+-----+
    | datetime            | Vancouver | Portland | San Francisco | ... |
    | 2012-10-01 13:00:00 | 284.63    | 282.08   | 289.48        | ... |
    | 2012-10-01 14:00:00 | 284.6290  | 282.0832 | 289.4749      | ... |
    | 2012-10-01 15:00:00 | 284.6269  | 282.0918 | 289.4606      | ... |
    | ...                 | ...       | ...      | ...           | ... |
    +---------------------+-----------+----------+---------------+-----+

    And convert it into this format:
    +---------------------+---------------+-------------+-----+
    | datetime            | city          | temperature | ... |
    | 2012-10-01 13:00:00 | Vancouver     | 284.63      | ... |
    | 2012-10-01 13:00:00 | Portland      | 282.08      | ... |
    | 2012-10-01 13:00:00 | San Francisco | 289.48      | ... |
    | 2012-10-01 14:00:00 | Vancouver     | 284.6290    | ... |
    | 2012-10-01 14:00:00 | Portland      | 282.0832    | ... |
    | 2012-10-01 14:00:00 | San Francisco | 289.4749    | ... |
    | 2012-10-01 15:00:00 | Vancouver     | 284.6269    | ... |
    | 2012-10-01 15:00:00 | Portland      | 282.0918    | ... |
    | 2012-10-01 15:00:00 | San Francisco | 289.4606    | ... |
    | ...                 | ...           | ...         | ... |
    +---------------------+---------------+-------------+-----+

    The reason for this is that variables should never be spread across
    columns. In this case, each city has its own column, which violates
    principles of data management. Even though the contents is the same, the
    second data format is far easier to analyze with something like Pandas
    than the first. The new format also allows all the weather data to be
    stored in one table, rather than the raw weather data which is spread
    across multiple csvs for each type of data (temperature, humidity, etc.)
    """

    # Open a connection to the sqlite database
    with db.get_conn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_WEATHER_TABLE)

        # Open each of the data files
        files = [ut.get_data_file(file) for file in re.DATA_FILES]
        # Create csv readers for each file
        readers = [csv.reader(f) for f in files]

        # Get the headers from each csv file to omit the first row
        headers = [next(r) for r in readers]

        # Confirm that all the headers are the same between the various data
        # files. If not, log a warning
        if not ut.is_homogeneous(headers):
            print("Warning: headers don't match:", headers)

        # Create progress bar based on the expected number of rows that will
        # be added. (This is the number of rows in one of the data files,
        # sans the header row, times the number of cities)
        expected_rows = (ut.get_data_file_lines('temperature.csv') - 1) * \
                        (len(headers[0]) - 1)
        progress_bar = tqdm(total=expected_rows, desc='Reading data...')

        # Iterate through each data file simultaneously
        for temp, hum, pre, w_desc, w_dir, w_spd in zip(*readers):
            rows = (temp, hum, pre, w_desc, w_dir, w_spd)

            # Get the timestamp from the temperature file
            timestamp = ut.format_time(temp[0])

            # Check to make sure that the data lines up between all the
            # different data files.

            # If all the timestamps aren't the same, log a warning and continue
            if not ut.is_homogeneous([ut.format_time(t[0]) for t in rows]):
                print("Warning: timestamps don't match:", rows)
            # If the rows don't have the same number of columns, log a warning
            if not ut.is_homogeneous([len(r) for r in rows]):
                print("Warning: rows have inconsistent column counts:", rows)

            # Assuming the data lined up and is good, send the data point for
            # each city to the database.
            for i in range(1, len(rows[0])):
                progress_bar.update(1)
                conn.execute(
                    sql.ADD_WEATHER_DATA,
                    (timestamp, headers[0][i]) + tuple([r[i] for r in rows])
                )

        # Close each of the data files
        for f in files:
            f.close()

        progress_bar.close()
