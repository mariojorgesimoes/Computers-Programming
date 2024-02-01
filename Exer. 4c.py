# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:14:02 2019

@author: Alunos
"""

#Números primos apresentados sob a forma de lista

n= int( input('Apresentar números primos até...'))

for j in range(2,n):
    for i in range(2,j):
        if ( j%i == 0 ):
            break
    else:   
        lista=[]
        lista.append(j)
        print (lista)