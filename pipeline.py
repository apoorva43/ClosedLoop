'''
Code to visualize the signals for all 24 channels - before and after processing each epoch.
'''

import argparse
import numpy as np
from process import *
from parameters import *
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Read channel number as command line argument
parser = argparse.ArgumentParser()
parser.add_argument("--channel", "-c", help="channel number from 0-23")
args = parser.parse_args()
ch = args.channel
ch = int(ch)

# Load raw EEG data from .mat file
data = loadmat('Matlab/eeg_data.mat')
eeg_data = data['eeg_data']

# Processing without channel projection
num_trials = 1
epochs = []
for i in range(num_trials):
    eeg = eeg_data
    epoch = preproc1epoch(eeg)
    epochs.append(epoch)
    
# Plot before processing
channel = eeg_data[ch] 
x = np.arange(1, 724639)
y = channel
plt.plot(x, y, label = 'before-processing')
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['figure.dpi'] = 100 
plt.show()

# Plot after preocessing
channel_ = epochs[0][ch] 
x = np.arange(1, 724639)
y = channel_
plt.plot(x, y, label = 'after-processing')
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['figure.dpi'] = 100 
plt.show()