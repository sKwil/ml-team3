import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier


def train(training_features: pd.DataFrame,
          training_labels: pd.DataFrame) -> VotingClassifier:
    """
    Train the final ML model using the ideal hyper parameters found through
    testing elsewhere.

    :param training_features: the features to train on
    :param training_labels: the target labels for training
    :return: the trained model
    """

    # Create the model with the proper hyper parameters
    print('Creating MLPClassifier n')
    mpl_n = MLPClassifier(batch_size='auto', warm_start=True, max_iter=400,
                          activation='tanh', alpha=0.02, solver='adam',
                          hidden_layer_sizes=(60, 80, 100, 120),
                          verbose=1)

    print('Creating MLPClassifier a')
    mpl_a = MLPClassifier(batch_size='auto', warm_start=True, activation='tanh',
                          solver='adam', max_iter=400,
                          early_stopping=True, beta_1=0.5, beta_2=0.6,
                          alpha=0.000005,
                          hidden_layer_sizes=(60, 80, 100, 120),
                          verbose=1)

    print('Creating SVC')
    svc = SVC(C=5, gamma=2, kernel='rbf', verbose=1)

    print('Creating RandomForestClassifier')
    rf = RandomForestClassifier(warm_start=False, bootstrap=False, max_depth=16,
                                max_features='auto',
                                min_samples_leaf=2, n_estimators=12,
                                verbose=1)

    print('Creating KNeighborsClassifier')
    kn = KNeighborsClassifier(algorithm='brute', leaf_size=9,
                              metric='euclidean', n_neighbors=7, p=4,
                              weights='distance')

    # Train the model
    print('Creating VotingClassifier')
    voting_clf = VotingClassifier(
        estimators=[('mpl_n', mpl_n), ('mpl_a', mpl_a), ('svc', svc),
                    ('rf', rf), ('kn', kn)], voting='soft', verbose=1)

    print('Training full classifier...')
    voting_clf.fit(training_features, training_labels)

    # Return the trained model
    return voting_clf
