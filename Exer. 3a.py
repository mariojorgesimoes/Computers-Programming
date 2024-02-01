# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:44:49 2019

@author: mjorg
"""

N=int( input('Introduza um número N: ') )
a=float( input('Introduza a base, a: ') )

soma=0

for i in range (N+1):
    soma+=a**N
    
print(soma)