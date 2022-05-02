import os
from typing import IO, List
from datetime import datetime as dt

import model.data.resources as re
from model.data import db


def get_data_file(directory: str, file: str) -> IO:
    """
    Open a csv data file from the raw data directory.

    Args:
        directory: The name of the directory where the specified file is
                   stored. This should be a subdirectory within /data/raw.
        file: The name of the data file within the specified directory.

    Returns:
         The opened file.
    """

    return open(os.path.join(re.DATA_RAW_DIR, directory, file))


def is_homogeneous(items: List) -> bool:
    """
    Return whether the given list is homogeneous (meaning it contains only
    one item repeated an arbitrary number of times, rather than separate
    unique items). If there exists any two elements in a list that are not
    identical, the list is not homogeneous.

    :param items: the list of items to check
    :return: true if and only if the list contains only one unique element
    """

    if len(items) < 2:
        return True

    first = items[0]
    for i in items[1:]:
        if i != first:
            print('Found non-matching elements:\n -', first, '\n -', i)
            return False
    return True


def format_time(time_str: str) -> dt:
    """
    Format some string into a datetime object based on the format specified
    in resources.DATE_TIME_FORMAT.

    :param time_str: the time as a string
    :return: the datetime object
    """

    return dt.strptime(time_str, re.DATE_TIME_FORMAT)


def get_data_file_lines(file: str) -> int:
    """
    Count the number of lines in the given data file.

    Args:raw.
        file: The complete path to the file (see model.data.data_files.py)

    Returns:
         The number of lines in the file.
    """

    with open(file) as f:
        return sum(1 for _ in f)


def run_script(script_file: str):
    """
    Execute an arbitrary .sql file script on the weather database.
    :param script_file: the path to the file to execute
    """

    with db.get_conn() as conn:
        with open(script_file) as script:
            conn.executescript(script.read())


def get_stations_rows() -> int:
    """
    Retrieve the number of rows in the Cities table.
    :return: the number of rows in the Cities table
    """

    return get_row_count('Stations')


def get_row_count(table_name: str) -> int:
    """
    Retrieve the number of rows in the specified table/view from the sqlite
    database.
    :param table_name: the name of the table/view
    :return: the number of rows in the table
    """

    with db.get_conn() as conn:
        rows = conn.execute('SELECT COUNT(*) FROM {t};'.format(t=table_name))
        return rows.fetchall()[0][0]
