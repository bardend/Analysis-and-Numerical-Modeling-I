
from numpy import dot,sqrt,array,eye,zeros_like,cos,sin,diag,exp,pi
from numpy.linalg import solve
from math import *

import pandas as pd 
from tabulate import tabulate
print("Metodo de Broyden")
tabla = {  'x': [] , 'error': []}

def f(x):
    z = zeros_like(x)
    z[0] = 3*x[0]-cos(x[1]*x[2])-0.5
    z[1] = x[0]**2 -81*(x[1]+0.1)**2+sin(x[2])+1.06
    z[2] = exp(-x[0]*x[1])+20*x[2]+(10*pi-3)/3
    return z

def broyden(x0,A0):
    TOL = 1E-5
    MAXITER = 100
    k = 0
    xk = x0
    Ak = A0
    terminar = False
    tabla["x"].append(xk.flatten())
    tabla["error"].append("====")
    while not terminar:
        fk = f(xk)
        absfk = sqrt(dot(fk.T,fk))
        if absfk<TOL or k>MAXITER:
            terminar = True
        else:
            sk = solve(Ak,-fk)
            xk1 = xk + sk
            fk1 = f(xk1)
            yk = fk1 - fk
            Ak +=  (yk - Ak@sk)@sk.T *(1/dot(sk.T,sk)) 
            k += 1
            fk = fk1
            xk = xk1

            tabla["x"].append(xk.flatten())
            tabla["error"].append(absfk)
           
    df = pd.DataFrame(tabla)
    print(tabulate(df,headers = "keys",tablefmt = "fancy_grid"))          
        
    return xk

x0 = array([[0.1,0.1,-0.1]]).T

A0 = array([[3 , 9.999833*1e-4, -9.999833*1e-4],
            [0.2 , -32.4, 0.9950042],
            [-9.9004*1e-2 , -9.9004*1e-2 , 20]])
print(A0)
xk = broyden(x0,A0)
