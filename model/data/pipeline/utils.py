"""
These are utility methods for the pipeline package, particularly the
aggregate.py file.
"""
import pandas as pd

from model.data.pipeline import resources as re
from model import db


def load_sql_as_df(query: str) -> pd.DataFrame:
    """
    Execute the given SQL query and return the results as a Pandas Data Frame.

    :param query: the SQL query to execute
    :return: the result of the query as a Pandas Data Frame
    """

    with db.get_conn() as conn:
        return pd.read_sql_query(query, conn)
