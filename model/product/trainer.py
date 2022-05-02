import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train(training_features: pd.DataFrame,
          training_labels: pd.DataFrame) -> RandomForestClassifier:
    """
    Train the final ML model using the ideal hyper parameters found through
    testing elsewhere.

    :param training_features: the features to train on
    :param training_labels: the target labels for training
    :return: the trained model
    """

    # Create the model with the proper hyper parameters
    clf = RandomForestClassifier(max_depth=15,
                                 max_features='sqrt',
                                 min_samples_leaf=1,
                                 n_estimators=13,
                                 random_state=42)

    # Train the model
    clf.fit(training_features, training_labels)

    # Return the trained model
    return clf
