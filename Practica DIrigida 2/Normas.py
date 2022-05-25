import numpy as np
from numpy import linalg as LA
b = np.array([[1/3, 1/5], [5., 7.]])
print(b)
# Frobenius
Nf = LA.norm(b,'fro')
print("\nLa norma frobenius es: ",Nf)
# Inf -> derecha
print("La norma Inf es: ",LA.norm(b,np.inf))
# 1 ->up
print("La norma 1 es: ",LA.norm(b,1))