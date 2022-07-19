import numpy as np

from numpy import dot,sqrt,array,eye,zeros_like,cos,sin,diag,exp,pi
from numpy.linalg import solve
from math import *


def f(x):
    ft = np.zeros((3, 1))
    ft[0] = 3*x[0]-cos(x[1]*x[2])-0.5
    ft[1] = x[0]**2 -81*(x[1]+0.1)**2+sin(x[2])+1.06
    ft[2] = exp(-x[0]*x[1])+20*x[2]+(10*pi-3)/3
    return ft


def J(x):
    Jf = np.zeros((3, 3))
    Jf[:, 0] = np.transpose([3 , 2*x[0] , -x[1]*exp(-x[0]*x[1]) ])
    Jf[:, 1] = np.transpose([x[2]*sin(x[1]*x[2]) , -162*(x[1]+0.1) ,-x[0]*exp(-x[0]*x[1]) ])
    Jf[:, 2] = np.transpose([0 , cos(x[2]) , 20])
    return Jf


def homotopia(f, J, x0, N=8):
    k = 1
    h = 1/N
    a = f(x0)
    b = -1*h*a
    while k <= N:
        A = J(x0)
        k1 = ((np.linalg.inv(A)@ b)).T
        C = x0+(1/2*k1)
        C = C.ravel().tolist()
        D = J(C)
        k2 = ((np.linalg.inv(D)@ b)).T
        E = x0+(1/2*k2)
        E = E.ravel().tolist()
        F = J(E)
        k3 = ((np.linalg.inv(F)@ b)).T
        G = x0+k3
        G = G.ravel().tolist()
        I = J(G)
        k4 = ((np.linalg.inv(I)@ b)).T
        x = x0+(k1+2*k2+2*k3+k4)/6
        print("Iteracion", k, x[0])
        x0 = x.ravel().tolist()
        k = k+1


x0 = [0., 0., 0.]

print("x0 = [0., 0.]")
homotopia(f, J, x0)