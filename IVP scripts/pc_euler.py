# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 02:14:08 2023

@author: azman
"""
def pc_euler(A,y,x):
    
    import numpy as np
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        y0=y+delx[i-1]*np.dot(A(x[i-1],Y[i-1]),y)
        y+=delx[i-1]*np.dot(A(x[i],Y[i]),y0)
        Y[i]=y
        
    
    return Y

import numpy as np
def A(x,y):
    return np.array([[0,-1],[1,0]])
y=np.array([0.0,1])
t=np.linspace(0,2*100*np.pi,90000)
Y=pc_euler(A,y,t)
import matplotlib.pyplot as plt
plt.plot(t,Y[:,0],t,Y[:,1])