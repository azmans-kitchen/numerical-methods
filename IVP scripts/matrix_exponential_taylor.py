# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:57:43 2023

@author: azman
"""
def matexp(A,n=20):
    
    import numpy as np
    
    m=0
    if np.max(np.sum(np.abs(A),axis=0))>=0.5:
        m=np.ceil(np.abs(np.log(np.max(np.sum(np.abs(A),axis=0))))/np.log(2)).astype(int)+1
        A=A/(2.0**m)

    N=np.shape(A)[0]
    I=np.identity(N)
    X=np.zeros((N,N))
    for i in range(n):
        X+= I.copy()/np.math.factorial(i)
        I=np.dot(I,A)
    
    for i in range(m):
        X=np.dot(X,X)
    
    return X
    