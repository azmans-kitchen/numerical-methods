# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 01:07:58 2023

@author: azman
"""
def newtoninterp(xx,x,y):
    
    import numpy as np
    
    N=np.size(x)

    divdif=np.zeros((N,N))
    divdif[:,0]=y

    for i in range(1,N):
        for j in range(N-i):
            divdif[j,i]=(divdif[j+1,i-1]-divdif[j,i-1])/(x[j+i]-x[j])
    
    yy=xx*0
    yp=yy
    
    for i in range(N):
        yp=divdif[0,i]
        for j in range(i):
            yp*=xx-x[j]
        yy+=yp
    
    return yy


