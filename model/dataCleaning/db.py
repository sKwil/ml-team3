import csv
import os
import sqlite3
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
    """

    # Open a connection to the sqlite database
    with getConn() as conn:
        # Clear any existing city data
        conn.execute(sql.CLEAR_WEATHER_TABLE)


