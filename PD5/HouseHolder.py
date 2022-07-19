import numpy as np
import scipy.linalg as sl

def householder_iterations(A, b, iterations):    
    nrowA, ncolA = np.shape(A)
    Qt = np.identity(nrowA)
    R = 1*A

    for j in range(iterations):
        if np.allclose(R[j:, j], 0.0):
            pass
        else:
            phi = np.sqrt(sum(R[j:nrowA, j]**2))*np.sign(R[j,j])

            w = np.zeros((nrowA, 1))
            w[j:nrowA, 0] = R[j:nrowA, j]
            w[j,0] += phi

            beta = 1/sum(w[j:nrowA]**2)
            Hj = np.identity(nrowA) - 2*beta*np.dot(w, w.T)
        
            R = np.dot(Hj, R)
            Qt = np.dot(Hj, Qt)
            b = np.dot(Hj, b)

    Q = Qt.T

    return R, Q, b 

def householder(A, b):
    nrowA, ncolA = np.shape(A)
    if nrowA > ncolA:
        R, Q, b = householder_iterations(A, b, ncolA)
    else:
        R, Q, b = householder_iterations(A, b, nrowA-1)

    return R, Q, b

A =np.array([[2,-1,-1,0,0],
[-1,3,0,-2,0],
[-1,0,4,2,1],
[0,-2,2,8,3],
[0,0,1,3,9]])
b=np.array([[-1],[3],[1],[1],[2]])

R,Q,b = householder(A,b)
print("\n----------------------------")
print("\n La solución x es:\n")
print(b)    
print("\n----------------------------")

"""
    Transforma el sistema Ax=b --> (Qt)Ax = (Qt)b, donde (Qt)A = R, Qt: transpuesta de Q
    Ademas Qt = Hn Hn-1 ... H2 H1, donde Hi es la i-esima matriz de householder, que elimina la i-esima columna
"""
