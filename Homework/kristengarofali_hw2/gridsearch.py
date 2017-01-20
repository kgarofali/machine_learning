from __future__ import print_function
import numpy as np
import makedata


def calc_likelihood(N):

    """
    Does a brute force maximum likelihood calculation of 
    slope and intercept given a grid of values.

    Parameters
    ----------
    N: int, determines grid spacing 

    Returns
    -------
    beta_one, beta_zero values based on max likelihood estimation 

    """

    x,y,p = makedata.generate_data(2.,3.,5,10000)
    beta_zero_grid = np.linspace(-10,10,num=N)
    beta_one_grid = np.linspace(-10,10,num=N)

    grid_all = np.array(np.meshgrid(beta_zero_grid, beta_one_grid)).T.reshape(-1,2)

    ls = []
    for i in range(len(grid_all)):
        ls.append(makedata.compute_likelihood(x,y,grid_all[i][0],grid_all[i][1]))
    max_l, = np.where(ls == np.max(ls))
    return ls, grid_all[max_l]
    


if __name__ == "__main__":
    ls, betas = calc_likelihood(100)
    print("Estimated value for beta_zero: {0}".format(betas[0][0]))
    print("Estimated value for beta_one: {0}".format(betas[0][1]))
