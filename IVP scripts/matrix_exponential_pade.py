# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:57:48 2023

@author: azman
"""

def matexp_pade(A,n=10):
    
    import numpy as np
    
    m=0
    if np.max(np.sum(np.abs(A),axis=0))>=0.5:
        m=np.ceil(np.abs(np.log(np.max(np.sum(np.abs(A),axis=0))))/np.log(2)).astype(int)+1
        A=A/(2.0**m)

    N=np.shape(A)[0]
    I=np.identity(N)
    NN=np.zeros((N,N))
    DD=np.zeros((N,N),dtype='float64')
    

    for i in range(n+1):
        NN+= I.copy()*np.math.comb(n,i)/np.math.perm(2*n,i)
        DD+= I.copy()*np.math.comb(n,i)/np.math.perm(2*n,i) * ((-1)**i)
        I=np.dot(I,A)
        
    X=np.dot(np.linalg.inv(DD),NN)
    for i in range(m):
        X=np.dot(X,X)
            
    return X
