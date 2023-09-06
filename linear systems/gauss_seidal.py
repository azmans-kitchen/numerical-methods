# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:34:01 2023

@author: azman
"""
def gssolve(A,b,iter_limit=100):
    import numpy as np
    [Nrow, Ncol] = A.shape
    assert Nrow == Ncol
    N = Nrow
    assert b.size == N
    A=A+0.0
    b=b+0.0
    for i in range(N):
        D=A[i,i]+0.0
        b[i]=b[i]/D
        A[i]=A[i]/D
    U=np.triu(A,1)
    A=A-U
    x=np.zeros(N)
    x_old=x.copy()
    tol=1
    iteration=0
    while (tol>1e-10):
        x=b-np.dot(U,x_old)
        for i in range(N):
            x[i]-= np.dot(A[i,0:i],x[0:i]) 
        
        tol=np.sqrt(np.sum((x-x_old)**2)/N)
        x_old=x.copy()
        iteration+=1
        if(iteration%5==0):
            print("Iteration", iteration, ": residue is ", tol )
        if (iteration>iter_limit):
            break
    print("It took ", iteration, " iterations")
    return x

import numpy as np

# N = 100
# A = np.zeros((N,N))
# b = np.ones(N)

# for i in range(N):
#     A[i,i] = 2.5
#     if (i>0):
#         A[i,i-1] = -1
#     if (i < N-1):
#         A[i,i+1] = -1
n=100
A = np.random.randint(-10,10,(n,n))
np.fill_diagonal(A,np.random.randint(100,110,n))
x = np.random.randint(-10,10,n)
print("Matrix A is", A)
b=np.dot(A,x)
print("Vector b is", b)
print("We expect the solution to be " ,x)
xx = gssolve(A,b)
print("Our solution is", xx)