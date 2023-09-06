# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:40:02 2023

@author: azman
"""
def trapeziumint(f,a,b,n):
    
    import numpy as np
    
    h=(b-a)/n
    x=np.arange(a,b+h,h)
    fx=f(x)
    fx[0]*=0.5
    fx[n]*=0.5
    return np.sum(fx)*h

def f(x):
    import numpy as np
    return np.exp(-x**2)

a=0
b=1
n=128

integral= trapeziumint(f, a, b, n)
error= 0.746824132812427-integral
