# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 02:56:05 2023

@author: azman
"""
def matexpmethod_pade(A,y,x,n=8):
    
    import numpy as np
    from matrix_exponential_pade import matexp_pade
    delx=np.diff(x)
    y=np.double(y)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        y=np.dot(matexp_pade(delx[i-1]*A(x[i-1],y),n),y)
        Y[i]=y 
    
    return Y

import numpy as np
def A(x,y):
    return np.array([[0,-1],[1,0]])
y=np.array([0.0,1])
t=np.linspace(0,64*np.pi,320)
Y=matexpmethod_pade(A,y,t)
import matplotlib.pyplot as plt
plt.plot(t,Y[:,0],t,Y[:,1])