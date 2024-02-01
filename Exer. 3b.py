# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:42:32 2019

@author: mjorg
"""

N=int( input('Introduza um número N: ') )

soma=0

for i in range (N+1):
    soma+=i
    
print(soma)