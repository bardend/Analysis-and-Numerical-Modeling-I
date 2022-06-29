import numpy as np

def gram_schmidt(A):
    Q = np.eye(A.shape[0])
    R = np.eye(A.shape[0])
    for i in range(0, A.shape[0]):
        R[i,i] = np.linalg.norm(A[:,i])
        Q[:,i] = A[:,i] / R[i,i]
        for j in range(i+1, A.shape[0]):
            R[i][j] = np.dot(Q[:,i], A[:,j])      
            A[:,j] = A[:,j] - np.dot(R[i,j], Q[:,i])
    return Q,R

        
        
def main():
    A = np.array([[1,1,1],[3,-1,-1],[2,-3,1]], dtype=float)
    b = np.array([37,3,13], dtype=float)
    
    print('-'*60)
    print('\t\tGram - Schmidt')
    print('-'*60)
    Q, R = gram_schmidt(A)
    print('\nMatriz Q\n')
    print(np.round(Q,decimals=4))
    print('\nMatriz R\n')
    print(np.round(R,decimals=4))
    
    solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
    print("\nSolucion: \nx",np.round(solucion,decimals=4))
    
if __name__ == '__main__':
    main()