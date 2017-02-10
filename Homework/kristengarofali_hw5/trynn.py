import numpy as np
from astropy.io import ascii
import sys

def nearest_neighbor(slength, swidth, plength, pwidth):
    """
    Function to read in training set and return iris type in training
    set that is nearest to input params based on euclidean distance
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
    nearest, = np.where(distance == np.min(distance))
    return train['class'][nearest]

def do_nearest_neighbor(infile):
    """
    Function to read in test data and compute iris type for each point
    using nearest_neighbor

    Parameters
    ----------
    infile: string
        name of test data file

    Returns
    -------
    nn.out: file that contains nearest neighbor type and real classification

    """

    test = ascii.read(infile, names=['slength','swidth', 'plength', 'pwidth','class'])
    nn_class = []

    for i in range(len(test)):
        nn_class.append(nearest_neighbor(test['slength'][i], test['swidth'][i], test['plength'][i], test['pwidth'][i]))
    nn_class = np.array(nn_class)
    ascii.write([nn_class, test['class']], 'nn.out', names=['nn_class', 'class'], formats={'nn_class': '%s', 'class': '%s'})



if __name__ == "__main__":
    do_nearest_neighbor(sys.argv[1])
