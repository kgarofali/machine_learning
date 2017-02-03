import numpy as np
from astropy.io import ascii
import sys

def kde_setosa(h,slength,swidth,plength,pwidth):

    """
    Function to return kde for iris setosa 

    Paramters
    ---------
    h: float
        bandwidth (from some k-fold cross  validation, usually)
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
    p(x|C1), kde for iris setosa 

    """

    setosa = ascii.read('iris.setosa',names=['slength','swidth', 'plength', 'pwidth','class'])
    distance = ((slength-setosa['slength'])**2 +(swidth-setosa['swidth'])**2+(plength-setosa['plength'])**2+(pwidth-setosa['pwidth'])**2)**(1./2)
    kernel = (1./(np.sqrt(2*np.pi)*h))**4*np.exp(-(distance)**2/(2*h**2))
    kde_est = (1./len(setosa))*np.sum((kernel*distance))
    return kde_est


def kde_versicolor(h,slength,swidth,plength,pwidth):

    """
    Function to return kde for iris versicolor 

    Paramters
    ---------
    h: float
        bandwidth (from some k-fold cross  validation, usually)
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
    p(x|C2), kde for iris versicolor 

    """

    versicolor = ascii.read('iris.versicolor',names=['slength','swidth', 'plength', 'pwidth','class'])
    distance = ((slength-versicolor['slength'])**2 +(swidth-versicolor['swidth'])**2+(plength-versicolor['plength'])**2+(pwidth-versicolor['pwidth'])**2)**(1./2)
    kernel = (1./(np.sqrt(2*np.pi)*h))**4*np.exp(-(distance)**2/(2*h**2))
    kde_est = (1./len(versicolor))*np.sum((kernel*distance))
    return kde_est


def kde_virginica(h,slength,swidth,plength,pwidth):

    """
    Function to return kde for iris versicolor 

    Paramters
    ---------
    h: float
        bandwidth (from some k-fold cross  validation, usually)
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
    p(x|C3), kde for iris virginica 

    """

    virginica = ascii.read('iris.virginica',names=['slength','swidth', 'plength', 'pwidth','class'])
    distance = ((slength-virginica['slength'])**2 +(swidth-virginica['swidth'])**2+(plength-virginica['plength'])**2+(pwidth-virginica['pwidth'])**2)**(1./2)
    kernel = (1./(np.sqrt(2*np.pi)*h))**4*np.exp(-(distance)**2/(2*h**2))
    kde_est = (1./len(virginica))*np.sum((kernel*distance))
    return kde_est

def run_kde(h,file_path):
    """
    Function to classify test set using KDEs above 

    Parameters
    ----------
    h: float
        bandwidth
    file_path: string
        path to test set data

    Returns
    -------
    kde.out, containing kde values for diff classes, correct class

    """

    testtab = ascii.read(file_path, names=['slength','swidth', 'plength', 'pwidth','class'])
    kde_setosa_vals = np.zeros(len(testtab))
    kde_versicolor_vals = np.zeros(len(testtab))
    kde_virginica_vals = np.zeros(len(testtab))
    actual_class = testtab['class']

    for i in range(len(testtab)):
        kde_setosa_vals[i]= kde_setosa(h,testtab['slength'][i],testtab['swidth'][i], testtab['plength'][i],testtab['pwidth'][i])

        kde_versicolor_vals[i] = kde_versicolor(h,testtab['slength'][i],testtab['swidth'][i], testtab['plength'][i],testtab['pwidth'][i])

        kde_virginica_vals[i] = kde_virginica(h,testtab['slength'][i],testtab['swidth'][i], testtab['plength'][i],testtab['pwidth'][i])

    ascii.write([kde_setosa_vals, kde_versicolor_vals, kde_virginica_vals,actual_class], 'kde.out', names=['kde_setosa', 'kde_versi', 'kde_virginica', 'actual_class'], formats={'kde_setosa':'%.2e','kde_versi':'%.2e', 'kde_virginica': '%.2e', 'actual_class': '%s'})



if __name__ == "__main__":

    run_kde(float(sys.argv[1]),sys.argv[2])
