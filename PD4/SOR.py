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
     x=np.transpose(np.array([1.,1.,1.],float))
     i=0
     while np.linalg.norm(x-aux, np.inf)/np.linalg.norm(x, np.inf)>tol :
         aux=x
         x=np.dot(get_G(A,w),x)+w*np.dot(np.linalg.inv(get_D(A)-w*get_E(A)),b)
         i+=1
         if i <4:
            print('La solucion en la iteracion ',i,' es:',x)
         
         if i==100:
            return 'La solucion NO converge'
     print("La respuesta final es: ")
     return x

        


#probelma 1
A = np.array([[4,3,0], [3,4,-1],[0,-1,4]])

b= np.transpose(np.array([24,30,-24]))


SOR(A,b,1.25,1e-4)
    