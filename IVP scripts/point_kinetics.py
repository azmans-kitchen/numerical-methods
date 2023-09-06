# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:39:20 2023

@author: azman
"""

def pointkinetics(t, rho, beta_i=[0]*6, pngt=0, solver=0, n=6):
    
    import numpy as np
    
    rho_t=np.zeros(np.size(t))
    for i in range(np.size(t)): rho_t[i]=rho(t[i])
    import matplotlib.pyplot as plt
    plt.figure(0)
    plt.plot(t,rho_t)        
    
    lambda_i=np.array([0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01])

    BETA=np.sum(beta_i)
    
    if (BETA==0):
        beta_i=np.array([0.000215, 0.001424, 0.001274, 0.002568, 0.000748, 0.000273])
        BETA=np.sum(beta_i)
        print("Peforming calculation with a sample delayed neutron fractions: ", beta_i)
    
    if (pngt==0):
        pngt=2e-5
        print("Prompt neutron generation time not specified. performing calculation with 20 microseconds")
    
    if (solver==0):
        from IVPSolver import matexpmethod_taylor
        solver=matexpmethod_taylor
        print("Solving with Matrix Exponential using taylor series of order ", n )
    
    def matA(time,yy):
        import numpy as np
        A=np.zeros((7,7))
        A[0,0]=(rho(time)-1) * BETA/pngt
        A[0,1:7]=lambda_i
        for i in range(6):
            A[i+1,i+1]=-lambda_i[i]
            A[i+1,0]=beta_i[i]/pngt
        return A
        
    y=np.zeros(7)
    y[0]=1
    y[1:7]=beta_i/(pngt*lambda_i)
    y0=y.copy()
    
    Y=solver(matA,y,t,n)
    return (Y/y0).T, matA
    
import numpy as np, math
from IVPSolver import RK4, matexpmethod_taylor, matexpmethod_pade
t=np.cumsum([0]+[np.pi/800]*1600)

#sample functions for reactivity variation
def rho(t):
    return -0.01*(t<10)

def rho1(t):
    import math
    return 0.1*math.sin(1*t)*math.exp(-0.0*t)

def rho2(t):
    import math
    return 0.5*t*(t<1)+ 0.5*math.exp(2*(1-t))*(t>=1)*(t<3)-3*math.exp(2*(3-t))*(t>=3)

def rho3(t):
    return (t<0.1)*5*t + 0*0.5*(t>=1)

def rho4(t):
    return (t<1)*-0.5*t - (t>=1)*(t<2)*4

Z,matA=pointkinetics(t, rho=rho2, solver=matexpmethod_taylor, n=6)
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(t,Z[0],".-",t,Z[1],"-",t,Z[2],"-",t,Z[3],"-",t,Z[4],"-",t,Z[5],"-",t,Z[6],"-")



