from __future__ import print_function 
import numpy as np
import sys


def calculate_print_mean(data_path):

    """
    Function to calculate and print mean given data file. 
    
    Parameters
    ----------
    data_path: string
        path name to file 
    
    Returns
    -------
    mean of data from file 
    
    """

    xs = np.genfromtxt(data_path)
    print("Mean value from data.out: {0}".format(np.mean(xs)))


if __name__ == "__main__":

    calculate_print_mean(sys.argv[1])
