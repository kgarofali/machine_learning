from __future__ import print_function 
import numpy as np
import sys

def bootstrap_resample(M, data_path):

    """
    Function to do bootstrap resampling of array 

    Parameters
    ----------
    M: int 
        number of resamples to do  
    data_path: string
        path to file with original data 

    Returns
    -------
    boot.out: file containing mean of each resample set 

    """

    xs = np.genfromtxt(data_path)
    means = []
    for i in range(M):
        resampled_xs = np.random.choice(xs,len(xs),replace=True)
        print("Mean value for {0} resample: {1}".format(i,np.mean(resampled_xs)))
        means.append(np.mean(resampled_xs))

    np.savetxt('boot.out', np.array(means), fmt='%.4f')

    
if __name__ == "__main__":

    bootstrap_resample(int(sys.argv[1]), sys.argv[2])

