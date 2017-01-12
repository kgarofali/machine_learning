import numpy as np
from astropy.io import ascii

def generate_data(x,a,b, mu, sigma):
    """
    Generates N pairs of points (x_i,y_i) with a 
    noise term. 
    
    Parameters
    ----------
    x: array, independent varialbe
    a: float, slope 
    b: float, intercept
    mu: float, mean of gaussian distribution
    sigma: float, std dev of gaussian distribution

    Returns
    -------
    data.out: file containing x,y pairs of points generated from linear eq  
    
    """

    epsilon = np.random.normal(loc=mu, scale=sigma, size=len(x))
    y = a*x + b + epsilon
    np.savetxt('data.out', np.transpose([x, y]), fmt=['%.4f', '%.4f'])
    return zip(x,y)


    
if __name__ == "__main__":
    x_arr = np.random.uniform(0,10,size=1000)
    a = 1.
    b = 2.
    mu = 0.
    sigma = 0.1
    generate_data(x_arr, a, b, mu, sigma)
