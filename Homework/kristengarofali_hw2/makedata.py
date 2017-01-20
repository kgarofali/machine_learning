import numpy as np
import matplotlib.pyplot as plt 

def generate_data(beta_zero, beta_one, lim, N):

    """
    Generates N x,y pairs given some beta_one, beta_zero, and lim,
    which are used to calculate a probability. 

    Parameters
    ----------
    beta_zero: float, intercept
    beta_one: float, slope
    lim: int, boundaries for x values
    
    Returns
    -------
    x,y: arrays of size N
    p: array, probability

    """

    xs = np.random.uniform(-lim,lim,size=N)
    p = 1./(1+np.exp(-(beta_zero+(beta_one*xs))))
    y_tmp = np.linspace(0,1,num=N)
    ys = np.zeros(len(y_tmp))
    for i in range(len(p)):
        if y_tmp[i] > p[i]:
            ys[i] = 0
        elif y_tmp[i] < p[i]:
            ys[i] = 1
    return xs,ys, p 

def compute_likelihood(xs,ys,beta_zero,beta_one):

    """
    Computes likelihood(beta_zero,beta_one) given x,y pairs of points.
    
    Parameters
    ----------
    xs: array, independent var 
    ys: array, dependent var 
    beta_zero: float, intercept
    beta_one: float, slope 

    Returns
    -------
    L: arr of float, likelihoods for the x,y pairs of points 

    """
    L=np.sum(ys*(beta_zero+(beta_one*xs))-np.log(1+np.exp(beta_zero+(beta_one*xs))))
    return L
    

if __name__ == "__main__":
    beta_zero = 2.
    beta_one = 3.
    lim = 5 
    N = 10000
    x,y, p = generate_data(beta_zero, beta_one, lim, N)
    plt.plot(x,p,'.')
    plt.ylim([-0.1,1.1])
    plt.xlabel('x')
    plt.ylabel('p')
    plt.savefig('part_b.png', format='png')
    plt.show()
            
    
    
