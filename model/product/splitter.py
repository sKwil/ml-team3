from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


def split(station_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame,
                                             pd.DataFrame, pd.DataFrame]:
    """
    Perform a stratified train-test-split on the station data. It is expected
    that the given station_df will be the cleaned data.

    The longitude column in the cleaned data is used to stratify the split.

    :param station_df: all the cleaned station data, ready for splitting
    :return: a tuple containing the following: (training features, testing
             features, training labels, testing labels)
    """

    # Add a column to the dataframe that classifies the longitude values into
    # bins for stratification.
    station_df['longitude_bin'] = pd.cut(station_df['longitude'],
                                         bins=[-400, -125, -100, -75, np.inf],
                                         labels=[1, 2, 3, 4])

    # Drop the original longitude column, as it's not necessary anymore
    station_df = station_df.drop('longitude', axis=1)

    # Perform a train test split and return the result
    return train_test_split(
        station_df.drop(['state', 'longitude_bin'], axis=1),
        station_df['state'],
        stratify=station_df['longitude_bin'],
        test_size=0.2,
        random_state=42)
