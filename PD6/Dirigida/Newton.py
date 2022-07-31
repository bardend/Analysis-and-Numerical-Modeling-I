import numpy as np

import pandas as pd 
from tabulate import tabulate
tabla = {'x':[]  , 'error':[]}

eps = 1E-4
xtol= 1E-4
maxIter = 100
f = lambda x: x**3-4*x+1
df = lambda x: 3*x**2-4 #derivada

x0 = 0.5
f0 = f(x0)
df0 = df(x0)
i = 0
h=None


tabla["x"].append(x0)
tabla["error"].append("=====")


while i < maxIter:
    h = -f0 / df0
    xold = x0
    x0 = x0 + h
    f0 = f(x0)
    df0 = df(x0)
    i += 1
    e=np.linalg.norm(x0-xold)
    tabla["x"].append(x0)
    tabla["error"].append(e)

    if abs(x0) <= xtol or abs(f0) <= eps:
        break
df = pd.DataFrame(tabla)
print(tabulate(df,headers = "keys",tablefmt = "fancy_grid"))

if abs(f0) >= eps:
    print("no converge")
else:
    print(f"Solución c={x0:5.4f}")
    print(f"iteraciones={i}")