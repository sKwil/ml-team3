import os
import sqlite3
import pandas as pd

WORKING_DIR = os.getcwd()

DATA_DIR = os.path.join(
    os.path.abspath(os.path.join(WORKING_DIR, os.pardir, os.pardir)),
    'data'
)

SQL_DIR = os.path.join(DATA_DIR, 'sql')

DATABASE = os.path.join(SQL_DIR, 'weather.db')


def getConn() -> sqlite3.Connection:
    """
    Get a connection to the sqlite database where all the weather data is
    stored.

    :return: a sqlite connection
    """

    return sqlite3.connect(DATABASE)


def getDataFrame():
    """
    convert the weather sqlite table into pandas data frame
    """

    # Get the connection to the table of interest. Currently set as the USWeather view.
    with getConn() as conn:
        df = pd.read_sql_query("SELECT * FROM USWeather", conn)

    return df
