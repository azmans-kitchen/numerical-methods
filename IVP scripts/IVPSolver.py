# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:19:44 2023

@author: azman
"""
def for_euler(A,y,x,n):
    
    import numpy as np
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        y+=delx[i-1]*np.dot(A(x[i-1],Y[i-1]),y)
        Y[i]=y
    
    return Y

def back_euler(A,y,x,n):
    
    import numpy as np
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        X=np.identity(ysize)-delx[i-1]*A(x[i],Y[i])
        y=np.linalg.solve(X,y)
        Y[i]=y
        
    
    return Y

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

def trapezoidal(A,y,x,n):
    
    import numpy as np
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        y0=y+delx[i-1]*np.dot(A(x[i-1],Y[i-1]),y)/2
        X=np.identity(ysize)-delx[i-1]*A(x[i],Y[i])/2
        y=np.linalg.solve(X,y0)
        Y[i]=y
            
    return Y

def heuns(A,y,x,n):
    
    import numpy as np
    delx=np.diff(x)
    
    ysize=np.size(y)
    ylen=np.size(x)
    Y=np.zeros((ylen,ysize))
    Y[0]=y
    
    for i in range(1,ylen):
        y0=y+delx[i-1]*np.dot(A(x[i-1],Y[i-1]),y)
        y+=delx[i-1]*(np.dot(A(x[i-1],Y[i-1]),y0)+np.dot(A(x[i],Y[i]),y))/2
        Y[i]=y
    
    return Y

def RK4(A,y,x,n):
    
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

