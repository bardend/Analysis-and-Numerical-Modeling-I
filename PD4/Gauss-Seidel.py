import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
import pandas as pd 
from tabulate import tabulate
tabla = {'x':[] , 'error':[]}

def get_D(A):
    D=np.diag(np.diag(A))
    return D #Retorna la diagonal

def get_L(A):
    n=len(A)
    E=np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            E[i][j]=A[i][j]
    return E # RETORNA EL LOW 

def get_U(A):
    return (A-get_D(A)-get_L(A))  # RETURN EL UP

def get_MGS(A):
    return -1*np.dot(np.linalg.inv(get_D(A)+get_L(A)),get_U(A))

def get_C(A,b):
    return    np.dot(np.linalg.inv(get_D(A)+get_L(A)),b)

def GaussSeidel(A,b,x,error):
    xk  = x
    tabla["x"].append(xk.flatten())
    tabla["error"].append("=====")
    
    iter  = 40
    mgs = get_MGS(A) 
    c = get_C(A,b)
    for i in range(iter):
        xk1 = np.dot(mgs,xk) + c      
        if np.linalg.norm(xk1-xk, np.inf)<error :
            print("Se termina en la iteacion" ,i)
            break 
        tabla["x"].append(xk.flatten())
        tabla["error"].append(np.linalg.norm(xk1-xk, np.inf))
        xk = xk1    
    
    df =  pd.DataFrame(tabla)
    print(tabulate(df,headers = "keys",tablefmt = "fancy_grid"))

    
A = np.array([[4,3,0], [3,4,-1],[0,-1,4]])
b= np.transpose(np.array([24,30,-24]))
x0=np.transpose(np.array([1.,0.,0.],float))

GaussSeidel(A,b,x0,1e-4)
