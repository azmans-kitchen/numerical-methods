# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:18:26 2023

@author: azman
"""
def Gaussianint(f,a,b,n):
    
    import numpy as np
    
    x,w=np.polynomial.legendre.leggauss(n)
    a0=(a+b)/2
    a1=(b-a)/2
    x=a0+a1*x
    fx=f(x)
        
    return a1*np.dot(fx,w)

def f(x):
    import numpy as np
    return np.exp(-x**2)

a=0
b=1
n=10

integral= Gaussianint(f, a, b, n)
error= 0.746824132812427-integral