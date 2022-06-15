import numpy as np

 # UN CASO PARTICULAR ES CUANDO W=1 ES EL MÉTODO DE GAUSS-SEIDEL

def get_D(A):
    D=np.diag(np.diag(A))
    return D #Retorna la diagonal

def get_E(A):
    n=len(A)
    E=np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            E[i][j]=-A[i][j]
    return E # RETORNA EL -LOW 

def get_F(A):
    return get_D(A)-get_E(A)-A  # RETURN EL -UP


def get_G(A,w):
     n=len(A)
     G=np.zeros((n, n))
     G= np.dot(np.linalg.inv(get_D(A)-w*get_E(A)),((1-w)*get_D(A) + w*get_F(A)))
     return G

def SOR(A,b,w,tol):
     n=len(A)
     aux=np.zeros((n, 1))
     x=np.transpose(np.array([0,1,0],float))
     i=0
     while np.linalg.norm(x-aux, np.inf)>tol:
        # print('La solucion en la iteracion ',i,' es:',x)
         aux=x
         x=np.dot(get_G(A,w),x)+w*np.dot(np.linalg.inv(get_D(A)-w*get_E(A)),b)     
         i+=1
         if i==1000:
            return 'La solucion NO converge'
     if i!=1000:
        print(w)
        


#probelma 1
A = np.array([[15, 12, 25],[10, 7, 20],[20, 15, 30]],float)
b= np.transpose(np.array([2400,1320,3000]))

#A = np.array([[4, 3, 0],[3, 4, -1],[0, -1, 4]],float)

#b= np.transpose(np.array([24,30,-24]))
j = 0.1
while j<2:
    j+=0.02
    SOR(A,b,j,1e-4)
    