"""
This file contains the main methods for aggregating the Weather data. The
aggregated data can be passed to the model later for training.
"""

import pandas as pd
from model.data.pipeline import utils as ut
from model.data.pipeline import sql_strings as sql

__INDEX = ['city', 'year', 'month']


def get_agg_data_frame() -> pd.DataFrame:
    """
    This is the master aggregation method. It assembles and returns a Pandas
    dataframe containing the aggregate monthly weather data.

    :return: a Pandas data frame
    """

    return ut.load_sql_as_df(sql.GET_MONTHLY_DATA)
