import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

R = 1000
tol = 1e-4
def Max_des(A,b):
    n=len(A[0])
    xk = np.transpose(np.array([0,0,0]))
    print(xk)
    for k in range (1,R):
        xlast = xk 
        print("Iter " ,k," :")
        rk = b - np.dot(A,xk)
        alphak = np.dot(rk.T,rk) / np.dot(rk.T,np.dot(A,rk))
        xk = xk + alphak*rk
        print(xk)

        if np.linalg.norm(xk-xlast, np.inf)<tol :
            print("Se termina en la iteacion" ,k)
            break
    return xk
    
#A=[[2,-1,1],[3,3,9],[3,3,5]]
a = np.array([[1,2,4], [4,4,1],[2,3,4]])
b = np.transpose(np.array([35,34,42]))

x = Max_des(a,b)
print("Rpta :")
print(x)