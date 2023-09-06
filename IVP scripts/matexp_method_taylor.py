# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:40:23 2023

@author: azman
"""
def matexpmethod_taylor(A,y,x,n=20):
    
    import numpy as np
    from matrix_exponential_taylor import matexp
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        y=np.dot(matexp(delx[i-1]*A(x[i-1],y),n),y)
        Y[i]=y        
    
    return Y

import numpy as np
def A(x,y):
    return np.array([[0,-1],[1,0]])
y=np.array([0.0,1])
t=np.linspace(0,64*np.pi,500)
Y=matexpmethod_taylor(A,y,t)
import matplotlib.pyplot as plt
plt.plot(t,Y[:,0],t,Y[:,1])
#plt.yscale("log")