# Nos devuelve un vector con los autovalores y una matriz con los autovectores
import numpy as np
#X = np.array([[13,8,8], [-1,7,-2],[-1,-2,7]])
X = np.array([[5,-2,-3], [2,0,-2],[3,-2,-1]])
 
autovalores, autovectores = np.linalg.eig(X)
print(autovalores)
print("=====================")
print(autovectores)