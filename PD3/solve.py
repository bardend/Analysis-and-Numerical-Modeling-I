import numpy as np

a = np.array([[1,2,4], [0,-4,-15],[0,0,-0.25]])

b = np.array([35,-106,-1.5])

x = np.linalg.solve(a, b)

print(x)
