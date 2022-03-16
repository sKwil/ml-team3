import sqlite3
import resources as re


def getConn() -> sqlite3.Connection:
    """
    Get a connection to the sqlite database where all the weather data is
    stored.

    :return: a sqlite connection
    """

    print(re.DATABASE)

    return sqlite3.connect(re.DATABASE)


def install():
    """
    Run the initial setup for the sqlite database, creating the basic tables
    that will be used later.
    """

    with getConn() as conn:
        with open(re.DATABASE_SETUP_SCRIPT) as script:
            conn.executescript(script.read())


