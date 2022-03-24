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

    cm_pairs = __get_city_month_pairs().set_index(['city', 'month'])
    temperature = __get_aggregate_temperature()
    humidity = __get_aggregate_humidity()
    pressure = __get_aggregate_pressure()
    wind = __get_aggregate_wind_speed()
    descriptions = __get_aggregate_weather_descriptions()

    df = pd.merge(cm_pairs, descriptions, left_index=True, right_index=True,
                  how='inner')

    return df


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

    The aggregation strategy used here is to compute the mean of the
    temperatures for all hours at the midday phase only. This is done across
    all days in each month for each city.

    :return: the indexed series of temperatures data
    """

    # Get a data frame with city, month, and temperature columns
    df = ut.load_sql_as_df(sql.AGG_TEMPERATURE)
    # Return a series with city and month as indices and temperature as value
    return df.set_index(['city', 'month'])['temperature']


def __get_aggregate_humidity() -> pd.Series:
    """
        Get a series with aggregated humidity, indexed by unique city-month
        pairs.

        The aggregation strategy used here is to compute the mean of the
        humidity values for all hours at the midday phase only. This is done
        across all days in each month for each city.

        :return: the indexed series of humidity data
        """

    # Get a data frame with city, month, and humidity columns
    df = ut.load_sql_as_df(sql.AGG_HUMIDITY)
    # Return a series with city and month as indices and humidity as value
    return df.set_index(['city', 'month'])['humidity']


def __get_aggregate_pressure() -> pd.Series:
    """
        Get a series with aggregated pressure, indexed by unique city-month
        pairs.

        The aggregation strategy used here is to compute the mean of the
        pressure values for all hours at the midday phase only. This is done
        across all days in each month for each city.

        :return: the indexed series of pressure data
        """

    # Get a data frame with city, month, and pressure columns
    df = ut.load_sql_as_df(sql.AGG_PRESSURE)
    # Return a series with city and month as indices and pressure as value
    return df.set_index(['city', 'month'])['pressure']


def __get_aggregate_wind_speed() -> pd.Series:
    """
        Get a series with aggregated wind speed data, indexed by unique
        city-month pairs.

        The aggregation strategy used here is to compute the mean of the
        wind speed values for all hours at the midday phase only. This is done
        across all days in each month for each city.

        :return: the indexed series of wind speed data
        """

    # Get a data frame with city, month, and wind speed columns
    df = ut.load_sql_as_df(sql.AGG_WIND_SPEED)
    # Return a series with city and month as indices and wind speed as value
    return df.set_index(['city', 'month'])['wind_speed']


def __get_aggregate_weather_descriptions() -> pd.DataFrame:
    # Get a data frame with city, month, and relative frequencies for each
    # of the weather description types
    df = ut.load_sql_as_df(sql.AGG_WEATHER_DESCRIPTION)

    # Return the dataframe with the city and month moved to indices
    return df.set_index(['city', 'month'])
