# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:02:32 2023

@author: azman
"""
def Simpson38int(f,a,b,n):
    
    import numpy as np
    if (n%3 != 0):
        j=n%3
        print("Integer not a multiple of 3. Increase number of intervals by ",\
              3-j, " or decrease it by ", j,"." )
        return float("nan")
    
    h=(b-a)/n
    x=np.arange(a,b+h,h)
    fx=f(x)
    integral=0
    for i in range(n+1):
        if (i==0 or i==n):
            integral+=fx[i]
        elif (i%3==0):
            integral+=2*fx[i]
        else :
            integral+=3*fx[i]
    return integral*3*h/8

def f(x):
    import numpy as np
    return np.exp(-x**2)

a=0
b=1
n=4

integral= Simpson38int(f, a, b, n)
error= 0.746824132812427-integral