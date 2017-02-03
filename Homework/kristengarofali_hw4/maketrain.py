import random
import numpy as np 
from astropy.io import ascii
import sys

def create_data_files(file_path):

    """
    Function to take data set and randomly split it into training and test sets. 

    Paramters
    ---------
    file_path: string
        path to data file (iris.data)

    Returns
    -------
    iris.train and iris.test 
    
    """

    iristab = ascii.read(file_path)
    indices_train = random.sample(range(len(iristab)),140)
    train = iristab[indices_train]
    test = np.delete(iristab,indices_train)

    ascii.write(test, 'iris.test')
    ascii.write(train, 'iris.train')

if __name__ == "__main__":
    
    create_data_files(sys.argv[1])
