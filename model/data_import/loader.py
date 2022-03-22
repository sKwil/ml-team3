import pandas as pd
from .. import db


def get_data_frame():
    """
    convert the weather sqlite table into pandas data frame Get the
    connection to the table of interest. Currently, set as the USWeather view.
    """
    with db.get_conn() as conn:
        df = pd.read_sql_query("SELECT * FROM USWeather", conn)

    return df
