# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:48:16 2023

@author: azman
"""
def Simpson13int(f,a,b,n):
    
    import numpy as np
    if (n%2 == 1):
        print("Odd number of intervals. \
Give an even number")
        return float("nan")
    
    h=(b-a)/n
    x=np.arange(a,b+h,h)
    fx=f(x)
    integral=0
    for i in range(n+1):
        if (i==0 or i==n):
            integral+=fx[i]
        elif (i%2==1):
            integral+=4*fx[i]
        else :
            integral+=2*fx[i]
    return integral*h/3

def f(x):
    import numpy as np
    return np.exp(-x**2)

a=0
b=1
n=129

integral= Simpson13int(f, a, b, n)
error= 0.746824132812427-integral
