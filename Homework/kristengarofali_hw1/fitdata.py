from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys 



def least_squares(datfile):
    """
    Function to read in N pair of points from file and fit data to 
    y = ax + b 

    Parameters
    ----------
    datfile: string, csv file with x,y points

    Returns
    -------
    estimated intercept and slope values

    """

    x,y = np.genfromtxt('data.out', unpack=True)
    beta_one = (np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x**2) - np.mean(x)**2)
    beta_zero = np.mean(y) - beta_one*np.mean(x)

    print("Estimated value for a (slope): {0}".format(beta_one))
    print("Estimated value for b (intercept): {0}".format(beta_zero))
    return beta_zero, beta_one

def make_plots(datfile, beta_zero, beta_one):

    """
    Function to plot x,y data and associated fit 
    or residuals 

    Parameters
    ----------
    datfile: string, csv file with x,y points 
    beta_zero: float, estimated intercept from fit 
    beta_one: float, estimated slope from fit 
    
    Returns
    -------
    Aforementioned plots 

    """

    if datfile == 'data.out':
        title_first = 'Part (e)'
        fig_first = 'part_e_plot.png'
        title_next = 'Part (f)'
        fig_next = 'part_f_plot.png'
    elif datfile == 'data2.out':
        title_first = 'Part (j)'
        fig_first = 'part_j_plot.png'
        title_next = 'Part (k)'
        fig_next = 'part_k_plot.png'
        
        
    x,y = np.genfromtxt(datfile, unpack=True)

    def line_func(x, beta_zero, beta_one):
        return beta_one*x + beta_zero

    y_fit = line_func(x, beta_zero, beta_one)

    plt.plot(x,y,'.', alpha=0.5, label='Data')
    plt.plot(x,y_fit,'-',lw=2, color='red',label='Fit')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title_first)
    plt.savefig(fig_first, format='png')
    plt.show()

    plt.plot(x,y-y_fit,'.',alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('Residuals')
    plt.title(title_next)
    plt.savefig(fig_next, format='png')
    plt.show()
    

if __name__ == "__main__":
    beta_zero, beta_one = least_squares(sys.argv[1])
    make_plots(sys.argv[1], beta_zero, beta_one)
