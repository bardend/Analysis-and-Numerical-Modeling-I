import numpy as np
#Fiorella  Meza
print("Método de la secante")
eps=1E-5
maxIter=100

f = lambda x: x**3-3*x+4

x0=1
x1=2
f0=f(x0)
f1=f(x1)
i=0
while i<maxIter and abs(f1)>=eps:
    h=-f1*((x1-x0)/(f1-f0))
    x0=x1
    x1=x1+h
    f0=f1
    f1=f(x1)
    i+=1
    print(f'x{i}={x1:5.4f}  f(x{i})={f1:5.4f}')
if(abs(f1)>=eps):
    print("no converge")
else:
    print(f"Solución c = {x1:5.4f}")
    print(f"Iteraciones = {i}")