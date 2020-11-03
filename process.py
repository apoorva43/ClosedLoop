'''
Code for standardizing, scaling, artifact correction of EEG data.
'''

import mne
import parameters
import numpy as np
from scipy.signal import detrend


def analyzeVar(p, threshold):
    '''
    Analyzes computed SSP projection vectors and only uses a projection vector if the vector independently explains more variance than the specified threshold. 
    '''
    
    threshold_idx = []
    for count, val in enumerate(p):
        if val > threshold:
            threshold_idx.append(count)
            
    return threshold_idx


def computeSSP(EEG, info, threshold):
    '''
    Computes SSP projections of epoched EEG data.
    Returns a list of SSP projection vectors above the pre-defined threshold (variance explained).
    '''
    
    projs = mne.compute_proj_epochs(EEG, n_eeg=5, n_jobs=1, verbose=True)

    p = [projs[i]['explained_var'] for i in range(5)]

    # If variance explained is above the pre-defined threshold, use the SSP projection vector
    threshold_idx = analyzeVar(p, threshold)

    threshold_projs = [] # List with projections above the threshold
    for idx in threshold_idx:
        threshold_projs.append(projs[idx])
        
    return threshold_projs


def preproc1epoch(eeg, info=parameters.info, projs=[], SSP=parameters.SSP, reject_chs=parameters.rejectChannels,\
                  opt_detrend=parameters.detrend, SSP_threshold=parameters.thresholdSSP):
    '''    
    Preprocesses EEG data epoch-wise.      
    '''
    
    n_samples = eeg.shape[0]
    n_channels = eeg.shape[1]
    eeg = np.reshape(eeg.T,(1,n_channels,n_samples))
    tmin = parameters.baselineTime 
    
    # Linear detrending:
    if opt_detrend:
        eeg = detrend(eeg, axis=2, type='linear')
        
    epoch = mne.EpochsArray(eeg, info, tmin=tmin, baseline=None, verbose=False)
    
    # Channel rejection
    if reject_chs: 
        bads = parameters.channelNamesExcluded
        epoch.drop_channels(bads)
    
    # SSP correction
    if SSP:
        #projs = computeSSP(epoch, info, SSP_threshold)
        epoch.add_proj(projs)
        epoch.apply_proj()
           
    epoch = epoch.get_data()[0]
    
    return epoch