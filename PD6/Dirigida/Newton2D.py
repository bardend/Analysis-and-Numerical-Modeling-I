import numpy as np
import pandas as pd 
from tabulate import tabulate
tabla = {'x':[]  , 'error':[]}

def F(x):
    #funcion f1, funcion f2
    #manualmente
    f1=x[0]**2+x[1]*x[0]-77 
    f2=x[1]**2+x[1]*x[0]-44
    return np.array([f1,f2])

def dF(x):
    #matriz jacobiana introducir valores
    #manualmente .
    return np.array([[2*x[0]+x[1], x[0]],
                      [x[1],2*x[1]+x[0]]])

def Gauss(x0):
    N=100
    x=x0
    tabla["x"].append(x.flatten())
    tabla["error"].append("=====")
    for k in range (N):
        xold=x
        Jinv=np.linalg.inv(dF(x))
        x=x-np.dot(Jinv,F(x))
        e=np.linalg.norm(x-xold)
        tabla["x"].append(x.flatten())
        tabla["error"].append(e)
        if e<1e-4:
            break
    df = pd.DataFrame(tabla)
    print(tabulate(df,headers = "keys",tablefmt = "fancy_grid"))


x0 = np.array([1,0])
Gauss(x0)        
