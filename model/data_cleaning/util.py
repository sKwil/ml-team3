import os
from typing import IO, List
from datetime import datetime as dt

from .. import resources as re


def get_data_file(fileName: str) -> IO:
    """
    Open a csv data file from the raw data directory.

    :param fileName: the full name of the file to load (with the extension)
    :return: the opened file
    """

    return open(os.path.join(re.DATA_RAW_DIR, fileName))


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
    Count the number of lines in the given data file. The file is opened with
    util.getDataFile().

    :param file: the name of the data file to count
    :return: the number of lines in the file
    """

    with get_data_file(file) as f:
        return sum(1 for _ in f)
