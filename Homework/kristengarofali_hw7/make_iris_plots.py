import sys
import matplotlib.pyplot as plt
from astropy.io import ascii
import numpy as np
import pandas as pd
from pandas.tools.plotting import parallel_coordinates


def plot_on_plane(infile):

    iris_dat = ascii.read(infile, names=['slength', 'swidth', 'plength', 'pwidth', 'class'])
    setosa = iris_dat[np.where(iris_dat['class'] == 'Iris-setosa')]
    versicolor = iris_dat[np.where(iris_dat['class'] == 'Iris-versicolor')]
    virginica = iris_dat[np.where(iris_dat['class'] == 'Iris-virginica')]

    plt.plot(setosa['plength'], setosa['pwidth'], 'o', color='blue', label='setosa')
    plt.plot(versicolor['plength'], versicolor['pwidth'], 'o', color='red', label='versicolor')
    plt.plot(virginica['plength'], virginica['pwidth'], 'o', color='green', label='virginica')
    plt.legend(loc=2)
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.show()

def plot_parallel_coordinates(infile):

    iris_dat = pd.read_csv(infile, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    parallel_coordinates(iris_dat, 'class')
    plt.show()


if __name__ == "__main__":
    plot_on_plane(sys.argv[1])
    plot_parallel_coordinates(sys.argv[1])
