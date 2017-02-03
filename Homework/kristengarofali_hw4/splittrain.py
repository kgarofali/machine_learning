import numpy as np 
from astropy.io import ascii
import sys

def split_data_file(file_path):

    """
    Function to split trianing set into three classes. 

    Parameters
    ----------
    file_path: string
        path to data file (iris.train)

    Returns
    -------
    iris.setosa, iris.versicolor, iris.virginica 

    """

    traintab = ascii.read(file_path, names=['slength','swidth', 'plength', 'pwidth','class'])
    setosa = traintab[np.where(traintab['class'] == 'Iris-setosa')]
    versicolor = traintab[np.where(traintab['class'] == 'Iris-versicolor')]
    virginica = traintab[np.where(traintab['class'] == 'Iris-virginica')]

    ascii.write(setosa, 'iris.setosa')
    ascii.write(versicolor, 'iris.versicolor')
    ascii.write(virginica, 'iris.virginica')

if __name__ == "__main__":

    split_data_file(sys.argv[1])
