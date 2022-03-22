import sqlite3
import resources as re


def get_conn() -> sqlite3.Connection:
    """
    Get a connection to the sqlite database where all the weather data is
    stored.

    :return: a sqlite connection
    """

    return sqlite3.connect(re.DATABASE)
