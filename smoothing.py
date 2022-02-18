import numpy as np

def rolling(species, window=5):
    smoothed=[]
    for spec in species:
        smoothed.append(spec.rolling(window).mean())
    return smoothed

def binning(time, species, binning=5):
    #average datapoints
    spec_binned = np.empty([len(species), len(species[0]) // binning])
    time_binned = []
    #time_binned = time[::binning]
    for ind in range(len(species)):
        for i in range(len(species[ind]) // binning):
            spec_binned[ind,i] = (np.average(species[ind][binning*i:binning*(i+1)]))
            ### activate if time is non-uniform
            if ind == 0:
                time_binned.append((np.average(time[binning*i:binning*(i+1)])))
    return time_binned, spec_binned