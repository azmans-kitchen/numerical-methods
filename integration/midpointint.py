# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:37:03 2023

@author: azman
"""
def midpointint(f,a,b,n):
    
    import numpy as np
    
    h=(b-a)/n
    x=np.arange(a+(h/2),b,h)
    fx=f(x)
    
    return np.sum(fx)*h

def f(x):
    
    return 3*x**2

a=1
b=5
n=100

integral=midpointint(f, a, b, n)
