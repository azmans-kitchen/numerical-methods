# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 01:45:16 2023

@author: azman
"""
from spline import splineinterp, naturalspline 
from leastsquare import lsr,pol
from newtoninterp import newtoninterp
import numpy as np, matplotlib.pyplot as plt


def f(x):
    return 1/(1+x**4)

x=np.linspace(-5,5,21)
y=f(x)

xx=np.linspace(-5,5,1001)
ynewton=newtoninterp(xx,x,y)
yspline=splineinterp(xx,naturalspline(x,y))
ypol=pol(xx,lsr(x,y,6))

plt.plot(xx,f(xx),label='function')
plt.plot(xx,ynewton,label='newton polynomial')
plt.plot(xx,yspline,label='spline')
plt.plot(xx,ypol,label='leastsquare')
plt.legend()



