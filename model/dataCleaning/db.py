import csv
import os
import sqlite3
from datetime import datetime as dt
from typing import IO

import resources as re
import sqlStrings as sql


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


def getDataFile(fileName: str) -> IO:
    """
    Open a csv data file from the raw data directory.

    :param fileName: the full name of the file to load (with the extension)
    :return: the opened file
    """

    return open(os.path.join(re.DATA_RAW_DIR, fileName))


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

        with getDataFile('city_attributes.csv') as file:
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

    # Open a connection to the sqlite database
    with getConn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_WEATHER_TABLE)

        # Start by adding each city with just its temperature data
        with getDataFile('temperature.csv') as file:
            # Read and parse the temperature csv
            r = csv.reader(file)
            header = next(r)

            # For each row in the csv (except the header), get the timestamp.
            # Then iterate over the rest of the cells in the row, matching them
            # with the column name in the header and sending to the database.
            for row in r:
                timestamp = dt.strptime(row[0], re.DATE_TIME_FORMAT)

                for i in range(1, len(row)):
                    conn.execute(sql.ADD_WEATHER_TEMPERATURE,
                                 (timestamp, header[i], row[i]))

        # Load each of the remaining weather data types and update the
        # Weather table accordingly.
