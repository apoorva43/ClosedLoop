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

# all channels in the system
channelNames = ['P7','P4','Cz','Pz','P3','P8','O1','O2','T8','F8','C4','F4','Fp2','Fz','C3','F3','Fp1',\
                'T7','F7','Oz','PO3','AF3','FC5','FC1','CP5','CP1','CP2','CP6','AF4','FC2','FC6','PO4']
#montage = 'standard_1020' 
info = createInfoMNE(channelNames, sampling_freq=100)

rejectChannels = True
channelNamesSelected =  ['Cz'] # concetrate only on the Cz channel
channelNamesExcluded = list(set(channelNames) - set(channelNamesSelected))

detrend = True # linear detrending of EEG signal 
SSP = True # apply SSP artifact correction
thresholdSSP = 0.1 # variance threshold for rejection of SSP projections
