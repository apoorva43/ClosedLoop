'''
Contains parameters for processing of EEG data.
'''

import mne

def createInfoMNE(channel_names, sampling_freq):
    '''
    Function to create an MNE info data structure.
    '''
    
    channel_types = ['eeg'] * len(channel_names)        
    info = mne.create_info(channel_names, sampling_freq, channel_types)
    
    return info

# Parameters

baselineTime = -0.1 # baseline for each epoch (seconds)

# channel names accoring to the .mat file contents
channelNames = ['Fp1','Fp2','F3','F4','C3','C4','P3','P4','O1','O2','F7','F8',\
                'FC3','FC4','P7','P8','Fz','Cz','Pz','FCz','Oz','AFz','CPz','POz'] 
#montage = 'standard_1020' 
info = createInfoMNE(channelNames, sampling_freq=100)

rejectChannels = True
channelNamesExcluded = ['Fp1','Fp2','F7','F8']
channelNamesSelected = list(set(channelNames) - set(channelNamesExcluded))

detrend = True # linear detrending of EEG signal 
SSP = True # apply SSP artifact correction
thresholdSSP = 0.1 # variance threshold for rejection of SSP projections

# Added new parameters - for new functions in process.py
highPass = 0  
lowPass = 40 
filterPhase = 'zero-double'
samplingRateResample = 250 # resample to 250 Hz