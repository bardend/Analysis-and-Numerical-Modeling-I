

import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
def raya():
  print("=======================") 

def LU_rectangle(A):
    n,m =  np.shape(A)
    L = np.zeros([n,n])
    for i in range(min(m,n)):
        L[i][i] = 1
        raya()
        print("Factores de la iteracion" ,i+1 ,":")
        for j in range(i+1,n):
            fact = -(A[j][i]/A[i][i])
            print(fact)    
    
            for k in range(m): #For matrix A
                A[j][k] = A[j][k] + (fact*A[i][k])
        
        
            L[j][i] = -(fact)    
            
        print(A)
    raya()
    print("L :")
    print(L) # This is Low
    print("U :")
    print(A) # This is Up 
    raya()
    print("convalidar")
    print(np.matmul(L,A)) #############CONVALIDATION#############
    
    #########################################################
    z=[[35],[34],[42]]
    R = np.linalg.solve(L, z)
    raya()
    print("R:")
    print(R)
    x = np.linalg.solve(A,R)
    raya()
    print("X:")
    print(x)

#A=[[1,4,7,2],[2,5,8,-1],[3,6,12,3]]
A=[[1,2,4],[4,4,1],[2,3,4]]

print(A)
    
LU_rectangle(A)

