import random
import numpy as np
import sys


def partition_data(infile, k):

    """
    Function to partition data into k slices

    Parameters
    ----------
    infile: string
        ascii file containing all data
    k: int
        number of folds (in this case 5)

    Returns
    -------
    partitioned_data (a list)

    """

    xdat, ydat = np.genfromtxt(infile, unpack=True)
    zipped_data = zip(xdat,ydat)
    random.shuffle(zipped_data)

    division = len(zipped_data)/float(k)
    return [ zipped_data[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(k) ]


def do_CV(partitioned_data, a, b):

    """
    Function to perform k-fold cross-validation

    Parameters
    ----------
    partitioned_data: list
        data partitioned into k sets from partition_data()
    a: float
        slope
    b: float
        intercept

    Returns:
    crossvalidate5.out data file containing average MSE from 5 iterations

    """

    def line_func(x, a, b):
        return a*x + b

    partitioned_data = partitioned_data

    mse_list = []
    for k in range(len(partitioned_data)):
        test = np.array(partitioned_data[k])
        train_partitioned = np.delete(partitioned_data,k,axis=0)
        train_full = np.vstack([x for i,x in enumerate(train_partitioned)])
        for i in range(len(train_full)):
            mse = (1./len(test))*np.sum((test[:,1]-line_func(train_full[i,0],a,b))**2)
        mse_list.append(mse)

    avg_mse = np.average(mse_list)
    print mse_list
    np.savetxt('crossvalidate5.out', [avg_mse])

if __name__ == "__main__":

    partitioned_data = partition_data(sys.argv[1],int(sys.argv[2]))
    do_CV(partitioned_data, float(sys.argv[3]), float(sys.argv[4]))
