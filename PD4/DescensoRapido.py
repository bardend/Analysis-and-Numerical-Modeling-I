import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
import pandas as pd 
from tabulate import tabulate
tabla = {'x':[] , 'rk' : [] , 'error':[]}
def Max_des(A,b,x,tol):
    xk  = x
    tabla["x"].append(xk.flatten())
    tabla["error"].append("=====")
    tabla["rk"].append("-----")
    iter  = 100 
    for i in range (iter):
        rk = b - np.dot(A,xk)
        num = np.dot(rk.T,rk)
        den = np.dot(np.dot(rk.T,A),rk)
        alphak = num / den
        xk1 = xk + alphak*rk 
        if np.linalg.norm(xk1-xk, np.inf)<tol :
            print("Se termina en la iteacion" ,i)
            break
        tabla["x"].append(xk.flatten())
        tabla["error"].append(np.linalg.norm(xk1-xk, np.inf))
        tabla["rk"].append(rk.flatten())

        xk  = xk1
    df  = pd.DataFrame(tabla)
    print(tabulate(df,headers = "keys",tablefmt = "fancy_grid"))
    return xk
    
#probelma 1
A = np.array([[3,3,4],
            [3,6,7],
			[4,7,11]],float)

b= np.transpose(np.array([6,9,11]))
x0=np.transpose(np.array([1.,1.,1.],float))
print(Max_des(A,b,x0,1e-3))