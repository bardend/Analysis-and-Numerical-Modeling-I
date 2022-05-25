import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

a = np.array([[1/3, 1/5], [5., 7.]])

ai =  inv(np.matrix(a))

print(ai)
