import numpy as np

def generate_data(N, mu, sigma):

    """
    Function to generate N points x_i from a gaussian 
    distribution.

    Parameters
    ----------
    N: int
        number of points to generate 
    mu: float 
        mean of gaussian
    sigma: float
        standard deviation of gaussian

    Returns
    -------
    data.out: file containing array of points x_i of length N 
    
    """


    xs = np.random.normal(loc=mu,scale=sigma,size=N)
    np.savetxt('data.out', xs, fmt='%.4f')


if __name__ == "__main__":
    mu = 0
    sigma = 1
    N = 1000
    generate_data(N,mu,sigma)
