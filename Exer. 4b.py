# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:50:37 2019

@author: Alunos
"""

#apresenta os números primos até n

n= int( input('Quantos números primos?'))

for j in range(2,n):
    for i in range(2,j):
        if ( j%i == 0 ):
            break
    else:
        print (j)

