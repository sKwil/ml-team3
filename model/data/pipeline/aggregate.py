"""
This file contains the main methods for aggregating the Weather data. The
aggregated data can be passed to the model later for training.
"""

import pandas as pd
from model.data.pipeline import utils as ut
from model.data.pipeline import sql_strings as sql


def get_agg_data_frame() -> pd.DataFrame:
    """
    This is the master aggregation method. It assembles and returns a Pandas
    dataframe containing the aggregate Weather data.
    :return: a Pandas data frame
    """

    cm_pairs = __get_city_month_pairs()

    return cm_pairs


# noinspection SqlResolve
def __get_city_month_pairs() -> pd.DataFrame:
    """
    Get a set of all the unique city-month pairs by grouping the data.
    :return: the city-month pairs as a Pandas Data Frame
    """

    return ut.load_sql_as_df(sql.CITY_MONTH_PAIRS)


def __get_aggregate_temperature() -> pd.Series:
    """
    Get a series with aggregated temperatures, indexed by unique city-month
    pairs.
    :return: the indexed series of temperatures
    """

    # Get a data frame with city, month, and temperature rows
    df = ut.load_sql_as_df(sql.AGG_TEMPERATURE)
    # Return a series with city and month as indices and temperature as value
    return df.set_index(['city', 'month'])['temperature']
