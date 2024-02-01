# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:47:52 2019

@author: Alunos
"""
from math import pi

n=1
p=1
delta=1

while delta>0.0001:
    
    p=p*( (4*n**(2) ) / (4*n**(2)-1) )
    delta = abs((pi/2)-p)
    n = n + 1
    
print('p=', p,)
print('delta=', delta)
print("n= ", n)