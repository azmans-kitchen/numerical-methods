# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 02:34:24 2023

@author: azman
"""
def RK4(A,y,x):
    
    import numpy as np
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        dy1=delx[i-1]*np.dot(A(x[i-1],y),y)
        dy2=delx[i-1]*np.dot(A(x[i-1]+0.5*delx[i-1],y+0.5*dy1),y+0.5*dy1)
        dy3=delx[i-1]*np.dot(A(x[i-1]+0.5*delx[i-1],y+0.5*dy2),y+0.5*dy2)
        dy4=delx[i-1]*np.dot(A(x[i],y+dy3),y+dy3)
        y+=(dy1+2*dy2+2*dy3+dy4)/6
        Y[i]=y        
    
    return Y

import numpy as np
def A(x,y):
    return np.array([[0,-1],[1,0]])
y=np.array([0.0,1])
t=np.linspace(0,2*np.pi,9)
Y=RK4(A,y,t)
import matplotlib.pyplot as plt
plt.plot(t,Y[:,0],t,Y[:,1])