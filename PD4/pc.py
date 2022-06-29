import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
import pandas as pd 
from tabulate import tabulate

c1 = np.array([1,2,3])
c2 = np.array([1,1,1])

M = np.dot(np.transpose(c1),c1) + 2*np.dot(np.transpose(c2),c2)

print(M)
