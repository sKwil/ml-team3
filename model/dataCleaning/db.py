import csv
import sqlite3
from tqdm import tqdm

import resources as re
import sqlStrings as sql
import util as ut


def getConn() -> sqlite3.Connection:
    """
    Get a connection to the sqlite database where all the weather data is
    stored.

    :return: a sqlite connection
    """

    return sqlite3.connect(re.DATABASE)


def install():
    """
    Run the initial setup for the sqlite database, creating the basic tables
    that will be used later.
    """

    with getConn() as conn:
        with open(re.DATABASE_SETUP_SCRIPT) as script:
            conn.executescript(script.read())


def loadCities():
    """
    Load the cities from the city_attributes.csv file and put them in the
    Cities table.

    Warning: This overwrites any existing data by first clearing the Cities
    table.
    """

    # Open a connection to the sqlite database
    with getConn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_CITIES_TABLE)

        with ut.getDataFile('city_attributes.csv') as file:
            # Skip the first row (the column headers)
            next(file)

            # Read the csv data one row at a time, sending it to the database
            r = csv.reader(file)
            c = 0
            for row in r:
                conn.execute(sql.ADD_CITY, (row[0], row[1], row[2], row[3]))
                c += 1

            print('Added', c, 'cities to SQL database')


def loadWeatherData():
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

    print('Loading weather data...')
    print('Importing data files...')

    # Open a connection to the sqlite database
    with getConn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_WEATHER_TABLE)

        # Open each of the data files
        files = [ut.getDataFile(file) for file in re.DATA_FILES]
        # Create csv readers for each file
        readers = [csv.reader(f) for f in files]

        # Get the headers from each csv file to omit the first row
        headers = [next(r) for r in readers]

        # Confirm that all the headers are the same between the various data
        # files. If not, log a warning
        if not ut.isHomogeneous(headers):
            print("Warning: headers don't match:", headers)

        # Create progress bar based on the expected number of rows that will
        # be added. (This is the number of rows in one of the data files,
        # sans the header row, times the number of cities)
        expected_rows = (ut.getDataFileLines('temperature.csv') - 1) * \
                        (len(headers[0]) - 1)
        print('Expected rows:', expected_rows)
        progress_bar = tqdm(total=expected_rows, desc='Reading data...')

        # Iterate through each data file simultaneously
        for temp, hum, pre, w_desc, w_dir, w_spd in zip(*readers):
            rows = (temp, hum, pre, w_desc, w_dir, w_spd)

            # Get the timestamp from the temperature file
            timestamp = ut.formatTime(temp[0])

            # Check to make sure that the data lines up between all the
            # different data files.

            # If all the timestamps aren't the same, log a warning and continue
            if not ut.isHomogeneous([ut.formatTime(t[0]) for t in rows]):
                print("Warning: timestamps don't match:", rows)
            # If the rows don't have the same number of columns, log a warning
            if not ut.isHomogeneous([len(r) for r in rows]):
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

        print('Successfully loaded weather data')
