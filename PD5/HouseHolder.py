import numpy as np
import scipy.linalg as sl

def householder_iterations(A, b, iterations):    
    nrowA, ncolA = np.shape(A)
    Qt = np.identity(nrowA)
    R = 1*A

    for j in range(iterations):
        print("**********************************************")
        if np.allclose(R[j:, j], 0.0):
            pass
        else:
            phi = np.sqrt(sum(R[j:nrowA, j]**2))*np.sign(R[j,j])
            print("La norma : \n",phi)
            w = np.zeros((nrowA, 1))
            w[j:nrowA, 0] = R[j:nrowA, j]
            w[j,0] += phi
            print("vector v1\n",w)
            beta = sum(w[j:nrowA]**2)
            print("(V1.T*V1)\n",beta)
            Hj = np.identity(nrowA) - 2*np.dot(w, w.T)/beta
            print("Hi\n",Hj)
            R = np.dot(Hj, R)
            Qt = np.dot(Hj, Qt)
            b = np.dot(Hj, b)
    print("Dont forget : Q = Hn-1*Hn-2*..H2*H1")
    print("Dont forget : R = QA")
        
    Q = Qt.T

    return R, Q, b 

def householder(A, b):
    nrowA, ncolA = np.shape(A)
    if nrowA > ncolA:
        R, Q, b = householder_iterations(A, b, ncolA)
    else:
        R, Q, b = householder_iterations(A, b, nrowA-1)

    return R, Q, b

A =np.array([[1,1],
            [1,-1],
            [1,-2]])
b=np.array([[13],[9],[0]])

R,Q,b = householder(A,b)
print("Q")
print(Q)
print("R")
print(R)
print("\n----------------------------")
print("\n La solución x es:\n")
print(b)    
print("\n----------------------------")

"""
    Transforma el sistema Ax=b --> (Qt)Ax = (Qt)b, donde (Qt)A = R, Qt: transpuesta de Q
    Ademas Qt = Hn Hn-1 ... H2 H1, donde Hi es la i-esima matriz de householder, que elimina la i-esima columna
"""
