'''
Code to implement Logisitic Regression on EEG data.
'''

import numpy as np
from sklearn.linear_model import LogisticRegression

def train_model(X, y, tol, C):
    '''
    Function to train a Logisitic Regression model on EEG data, binary labels.
    Returns a classifier object fit to X and y.
    '''
    clf = LogisticRegression(random_state=0, tol=tol, C=C)
    model = clf.fit(X, y)
    return model
    
def validate_model(X, y, valid_X, valid_y, tol, C):
    '''
    Function to find best set of hyperparameters on the validation dataset.
    Returns model accuracies. 
    '''
    clf = LogisticRegression(random_state=0, tol=tol, C=C)
    model = clf.fit(X, y)
    accuracy = model.score(valid_X, valid_y)
    return accuracy