import numpy as np
from astropy.io import ascii
import sys

def nearest_neighbor3(slength, swidth, plength, pwidth):
    """
    Function to read in training set and return iris types in training
    set that are three nearest points to input params based on euclidean distance
    between points.

    Parameters
    ----------
    slength: float
        sepal length in test set
    swidth: float
        sepal width in test set
    plength: float
        petal length in test set
    pwidth: float
        petal width in test set

    Returns
    -------
    iris type

    """

    train = ascii.read('iris.train', names=['slength','swidth', 'plength', 'pwidth','class'])
    distance = ((slength-train['slength'])**2 +(swidth-train['swidth'])**2+(plength-train['plength'])**2+(pwidth-train['pwidth'])**2)**(1./2)
    sorted_dists = np.argsort(distance)
    return train['class'][sorted_dists[0]], train['class'][sorted_dists[1]], train['class'][sorted_dists[2]]



def do_nearest_neighbor3(infile):
    """
    Function to read in test data and compute iris type for each point
    using nearest_neighbor3

    Parameters
    ----------
    infile: string
        name of test data file

    Returns
    -------
    nn3.out: file that contains nearest neighbor type for k=3 and real classification

    """

    test = ascii.read(infile, names=['slength','swidth', 'plength', 'pwidth','class'])
    nn_class = []

    for i in range(len(test)):
        nn_class.append(nearest_neighbor3(test['slength'][i], test['swidth'][i], test['plength'][i], test['pwidth'][i]))
    ascii.write([nn_class, test['class']], 'nn3.out', names=['nn_class', 'class'], formats={'nn_class': '%s', 'class': '%s'})

if __name__ == "__main__":
    do_nearest_neighbor3(sys.argv[1])
