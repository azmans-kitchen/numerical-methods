# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:44:24 2023

@author: azman
"""
Computing the maximum eigenvalue using power iteration
def eigenvalue(M,error=1e-6):
    
    import numpy as np
    
    Nx,Ny=np.shape(M)
    
    if (Nx!=Ny):
        print("Error: please provide a square matrix")
        return float("nan")
    
    N=Nx
    x=np.ones(N)
    ev=0
    tol=1
    
    while (tol>error):
        ev_old=ev
        x=np.dot(M,x)
        ev=np.max(np.abs(x))
        x=x/ev
        tol=ev-ev_old
    
    return ev,x

import numpy as np
M=np.array([[-7,13,-16],[13,-10,13],[-16,13,-7]])
ev,x=eigenvalue(M)

        
    
    
