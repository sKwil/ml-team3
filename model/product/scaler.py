import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def scale(training_features: pd.DataFrame) -> pd.DataFrame:
    """
    Perform scaling on the training data features.

    :param training_features: the training features to scale
    :return: the scaled training features
    """

    # Scaler with 0 as average
    scaler_std = StandardScaler()
    # Scaler based on min and max values
    scaler_min_max = MinMaxScaler()

    # Scale the data
    training_features = scaler_std.fit_transform(training_features)
    training_features = scaler_min_max.fit_transform(training_features)
    training_features += 1

    return training_features
