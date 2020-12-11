
% Script to get the EEG time series data from the .xdf file
% Reference for load_xdf: https://github.com/xdf-modules/xdf-Matlab

streams = load_xdf('pilotii102_braineii.xdf', 'HandleClockSynchronization', false);
temp = streams{1, 2}; % EEG data in 2nd struct
eeg_data = temp.time_series;
save('eeg_data.mat', "eeg_data");
% Sanity check for .mat file
whos -file eeg_data.mat
load eeg_data.mat
size(eeg_data)
