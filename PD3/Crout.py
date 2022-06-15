import numpy as np

def LU_decomposition(A):
    n=len(A[0])
    L = np.zeros([n,n])
    U = np.zeros([n, n])
    for i in range(n): #iterate eje -> , dow 
        
        U[i][i] = 1
        
        if i==0:
    
            L[0][0] = A[0][0]
            for j in range(1,n):
                L[j][0] = A[j][0]
                U[0][j] = A[0][j]/L[0][0]
        else :    
            for j in range(i,n): #iterate row
                temp = 0
                for k in range(0,n):
                    temp = temp + L[j][k]*U[k][i]
                L[j][i] = (A[j][i]-temp)/U[i][i]
            for j in range(i+1,n): #iterate col
                temp = 0
                for k in range(0,n):
                    temp = temp + L[i][k]*U[k][j]
                U[i][j] = (A[i][j]-temp)/L[i][i]            
    return L,U
    
#A=[[2,-1,1],[3,3,9],[3,3,5]]
A = np.array([[1,2,4], [4,4,1],[2,3,4]])
#b = np.array([[35],[34],[42]])
#A=[[1,2,4],[4,4,1],[2,3,4]]
(L,U) = LU_decomposition(A)
print("L")
print(L) 
print("U")
print(U) #ones
print(np.matmul(L, U))