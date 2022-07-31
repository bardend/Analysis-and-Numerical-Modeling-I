from numpy import dot,sqrt,array,eye,zeros_like,cos,sin,diag,exp,pi
from numpy.linalg import solve
from math import *
import numpy as np
import pandas as pd 
from tabulate import tabulate

def coc_Ray(A,x):
    return dot((A@x),x)/dot(x,x)
def m_pot(A,x0):
    
    maxiter = 100 
    tol =  1E-1
    k = 0 
    end =  False 
    while not end : 
        
        xnew = A@x0     
        if (k>maxiter or np.linalg.norm(xnew-x0,np.inf)<tol):
            end = True
        mini = np.amin(xnew)
        ret = xnew / mini
        k+=1     
        x0 = xnew

    print("El vector asociado es : ", ret) 
    print("El auto valor dominante es : ",coc_Ray(A,ret))
    
A0 = array([[0.7,0.3,0.1],[0.2,0.6,0.3],[0.1,0.1,0.6]])
x0 = array([42158,147553,21079]).T
m_pot(A0,x0)

## Metodo potencia inversa -> con desplazamiento (tablas)
## q = 0 , (init)   ; q  