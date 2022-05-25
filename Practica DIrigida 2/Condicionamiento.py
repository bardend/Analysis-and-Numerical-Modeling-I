import numpy as np
from numpy import linalg as LA

a = np.array([[1/3, 1/5], [5., 7.]])

print("Tomando la norma frobenius : ",LA.cond(a, 'fro'))

print("Tomando la norma infinito : ",LA.cond(a, np.inf))

print("Tomando la norma 1 : ",LA.cond(a, 1))

