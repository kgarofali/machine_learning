import numpy as np
import matplotlib.pyplot as plt
import sys


def plot_means(data_path, label):

    """
    Function to pllot histogram of means from resampling. 

    Parameters
    ----------
    data_path: string
        path to file containing data means
    label: string
        label for histogram/plot title 

    Returns 
    -------
    plots showing histograms of means 

    """

    means = np.genfromtxt(data_path)
    plt.hist(means,label=label,histtype='step')
    plt.title(label)
    plt.legend()
    plt.savefig(label+'.png', format='png')
    plt.show()


if __name__ == "__main__":
    plot_means(sys.argv[1],sys.argv[2])
