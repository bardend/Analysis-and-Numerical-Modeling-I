from cmath import pi
from numpy import sin,cos,tan

def rad_sex(angle):
    return (angle/180)*pi
eps = 1E-5
maxIter = 100
l = 2.2
h = 1.2
D = 0.75
beta1= rad_sex(11.5)

A = l*sin(beta1)
B = l*cos(beta1)
C = (h+0.5*D)*sin(beta1) - 0.5*D*tan(beta1)
E = (h+0.5*D)*cos(beta1)-0.5*D

f = lambda x: A*sin(x)*cos(x)+B*sin(x)**2-C*cos(x)-E*sin(x)

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