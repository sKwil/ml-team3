import pandas as pd
from .. import db


def get_data_frame(table: str) -> pd.DataFrame:
    """
    convert the weather sqlite table into pandas data frame Get the
    connection to the table of interest. Currently, set as the view from 'table' parameter.
    """
    with db.get_conn() as conn:
        df = pd.read_sql_query("SELECT * FROM {t};".format(t=table), conn)

    return df


def get_US_Weather_data() -> pd.DataFrame:
    """
    Get the USWeather SQL view as a Panda's DataFrame.
    :return: the dataframe
    """
    return get_data_frame('USWeather')


def get_weather_rows() -> int:
    """
    Retrieve the number of rows in the Weather table.
    :return: the number of rows in the Weather table
    """

    return get_row_count('Weather')


def get_cities_rows() -> int:
    """
    Retrieve the number of rows in the Cities table.
    :return: the number of rows in the Cities table
    """

    return get_row_count('Cities')


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
