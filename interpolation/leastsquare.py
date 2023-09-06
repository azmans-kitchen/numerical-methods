def lsr(x,y,k):
    
    import numpy as np

    n=np.size(x)
    mat=np.zeros((n,k+1))
    for nn in range(n):
        for kk in range(k+1):
            mat[nn,kk]= x[nn]**kk
    A=np.dot(mat.T,mat)
    b=np.dot(mat.T,y)
    alpha=np.linalg.solve(A,b)
    
    return alpha

def pol(x,alpha):
    import numpy as np
    n=np.size(alpha)
    y=x.copy()*0
    for i in range(n):
        y+=alpha[i]*x**i
    return y



    