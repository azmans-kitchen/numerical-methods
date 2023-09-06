# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 02:34:39 2023

@author: azman
"""
from matrix_exponential_taylor import matexp
from matrix_exponential_pade import matexp_pade
import scipy.linalg
expm=scipy.linalg.expm

import numpy as np
A=np.array([[-0.78125 ,   0.015625 ,  0.0234375], [ 0.0234375 , 0.03125 ,   0.0390625], [ 0.0390625,  0.046875 ,  0.0625   ]])#
print(expm(A))
print("Error with Taylor\n",matexp(A,10)-expm(A))
print("Error with Pade\n",matexp_pade(A,4)-expm(A))
A=np.array([[200,2,3],[3,4,5],[5,6,8]])
print(expm(A))
print("Error with Taylor\n",matexp(A,10)-expm(A))
print("Error with Pade\n",matexp_pade(A,4)-expm(A))
A=0.001*np.array([[0,-1],[1,0]])
print(expm(A))
print("Error with Taylor\n",matexp(A,10)-expm(A))
print("Error with Pade\n",matexp_pade(A,4)-expm(A))