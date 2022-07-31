from numpy import dot,sqrt,array,eye,zeros_like,cos,sin,diag,exp,pi
from numpy.linalg import solve
from math import *
import numpy as np
import pandas as pd 
from tabulate import tabulate


def coc_Ray(A,x):
    return dot((A@x),x)/dot(x,x)

def scale_pot(A,x0):
    maxiter = 100
    k = 0
    end = False
    tol = 1E-6

    while not end :
        xnew = A@x0 
        maxi = np.amax(xnew)
        xnew = xnew/maxi
        if(k>maxiter or np.linalg.norm(xnew-x0,np.inf)<tol):
            end = True 
        x0 = xnew
        k+=1    

    print("El auto valor dominante es : ",coc_Ray(A,xnew))    
    
A0 = array([[2,0,2],[-1,2,1],[0,1,4]])
x0 = array([1,1,0]).T 
scale_pot(A0,x0)