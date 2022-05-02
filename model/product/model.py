import pandas as pd
import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier

from model.product import cleaner
from model.product import splitter
from model.product import scaler
from model.product import trainer
from model.product import constants


def process() -> None:
    """
    This function run the entire machine learning process. It loads the
    data, cleans the data, performs a train-test-split, and scales the
    training data. Then it trains a final ML model using the ideal hyper
    parameters that we found through proper testing elsewhere, and saves the
    result in a pickle file.

    :return: None
    """

    # Load the training data and labels
    station_df = cleaner.get_cleaned_data()

    # Perform a train-test-split
    train_feat, test_feat, train_lab, test_lab = splitter.split(station_df)

    # Scale the training features
    train_feat = scaler.scale(train_feat)

    # Train the model
    model = trainer.train(train_feat, train_lab)

    # Save the trained model in the pickle file
    joblib.dump(model, constants.MODEL_FILE_PATH)
