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

    print('Populating Months Table...')
    ut.run_script(re.DB_MONTHS)

    print('Populating Regions Table...')
    ut.run_script(re.DB_REGIONS)

    print('Populating States Table...')
    ut.run_script(re.DB_STATES)

    print('Loading Weather Stations...')
    load_stations()
    print('  Added', loader.get_stations_rows(), 'stations to SQL database')

    print('Loading Precipitation Data...')
    load_monthly_data()

    print('Merging Monthly Data Raw...')
    print('  Loading...')
    ut.run_script(re.DB_MERGE_MONTHLY)

    print('Create Monthly Data View...')
    ut.run_script(re.DB_MONTHLY_DATA_VIEW)

    print('Cleaning Database...')
    ut.run_script(re.DB_SETUP_FINISH)

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

    rows = ut.get_data_file_lines(df.ALL_STATIONS)
    progress_bar = tqdm(total=rows, desc='Reading stations...')

    # Open a connection to the sqlite database
    with db.get_conn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_STATIONS_TABLE)

        with open(df.ALL_STATIONS) as file:
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


def load_monthly_data():
    """
    Load all the weather data from products/precipitation/* files.
    """

    p = df.PRECIPITATION_DIR
    t = df.TEMPERATURE_DIR

    # List the directory, data files, their corresponding SQL statements, and
    # the multiplying factor for correcting the units
    files = [
        (p, 'mly-prcp-50pctl.txt', sql.ADD_PRECIPITATION_MEDIAN, 0.01),
        (p, 'mly-prcp-avgnds-ge001hi.txt', sql.ADD_PRECIPITATION_DAYS_H, 1),
        (p, 'mly-prcp-avgnds-ge010hi.txt', sql.ADD_PRECIPITATION_DAYS_T, 1),
        (p, 'mly-prcp-normal.txt', sql.ADD_PRECIPITATION_NORMALS, 0.01),
        (p, 'mly-snow-50pctl.txt', sql.ADD_SNOWFALL_MEDIAN, 0.1),
        (p, 'mly-snow-avgnds-ge001ti.txt', sql.ADD_SNOWFALL_DAYS_T, 1),
        (p, 'mly-snow-avgnds-ge010ti.txt', sql.ADD_SNOWFALL_DAYS_I, 1),
        (p, 'mly-snow-normal.txt', sql.ADD_SNOWFALL_NORMALS, 0.1),
        (p, 'mly-snwd-avgnds-ge001wi.txt', sql.ADD_SNOW_DEPTH_DAYS, 1),
        (t, 'mly-tmax-normal.txt', sql.ADD_TEMP_MAX_NORMAL, 0.1),
        (t, 'mly-tmax-stddev.txt', sql.ADD_TEMP_MAX_STDEV, 0.1),
        (t, 'mly-tmin-normal.txt', sql.ADD_TEMP_MIN_NORMAL, 0.1),
        (t, 'mly-tmin-stddev.txt', sql.ADD_TEMP_MIN_STDEV, 0.1)
    ]

    # Total iterations is the total number of lines in every file, times 12
    # (for each month)
    total_iterations = sum([
        ut.get_data_file_lines(os.path.join(d, f)) for
        d, f, s, u in files
    ]) * 12

    progress_bar = tqdm(total=total_iterations,
                        desc='Reading monthly data...')

    # Connect to the SQLite database
    with db.get_conn() as conn:
        # Iterate for each data file in the precipitation folder
        for directory, file_name, sql_script, factor in files:
            # Open the file
            with open(os.path.join(directory, file_name)) as file:
                # Process each row in the file
                for row in file:
                    # Get the station id, and process the data for each month
                    station_id = row[0:11].strip()
                    for i in range(1, 13):
                        progress_bar.update(1)
                        value = float(row[11 + 7 * i:16 + 7 * i]) * factor
                        flag = row[16 + 7 * i].strip()
                        conn.execute(sql_script, (station_id, i, value, flag))
    progress_bar.close()
