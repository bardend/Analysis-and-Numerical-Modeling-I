from tabulate import tabulate
import numpy as np
tabla = { 'n':[] , 'x': [] , 'f(x)': []}
def puntofijo(f,x0):
    eps=1e-5
    maxIter=100
    f0=f(x0)
    i=0
    tabla["n"].append(i.__int__())
    tabla["x"].append(x0.__float__())
    tabla["f(x)"].append(f0)
    while i<maxIter and abs(f0-x0) >= eps:
        x0=f0
        f0=f(x0) 
        i+=1
        tabla["n"].append(i.__int__())
        tabla["x"].append(np.round(x0.__float__(),decimals=5))
        tabla["f(x)"].append(np.round(f0.__float__(),decimals=5))
    if abs(f0-x0)>=eps:
        print(f'Metodo no converge')
    else:
        print(tabulate(tabular_data=tabla,headers = "keys",tablefmt = "fancy_grid"))
        print(f'Solucion c={x0:5.5f}')
        print(f'Numero de iteraciones ={i}')
        
puntofijo(f=lambda x: (x**3+1)/4, x0=0.5)