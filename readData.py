'''
Code to read sample EEG data and binary category labels.
Data Reference: https://data.mendeley.com/datasets/sfwkmvmmd5/1
'''

import numpy as np
import scipy.stats as sc

def read_EEG():
    '''
    Function to read sample EEG data.
    Returns a numpy ndarray.
    '''
    data = np.load('Data/EEG_epochs_sample.npy')
    print(data.shape) # [1200, 550, 32]
    return data

def read_labels():
    ''' 
    Function to read sample binary category labels for the EEG data.
    Returns a numpy ndarray.
    '''
    labels = np.load('Data/y_categories_sample.npy')
    print(labels.shape) # [1200,]
    return labels

def normalize(data, axis=1):
    '''
    Function to scale and normalize the 3D EEG data array to a 2D array.
    Returns normalized numpy ndarray.
    '''
    trials = data.shape[0] # 1200
    samples = data.shape[1] # 550
    channels = data.shape[2] # 32
    data_new = np.reshape(data, (trials, samples * channels))
    return sc.zscore(data_new, axis=axis)

def read_npz():
    '''
    Function to read compressed version of EEG data (.npz file)
    Returns a numpy ndarray
    '''
    data = np.load('Data/EEG_epochs_compressed.npz')
    # print(data.files) # ['arr_0']
    print(data['arr_0'].shape) # [1200, 550, 32]
    return data['arr_0']
    
