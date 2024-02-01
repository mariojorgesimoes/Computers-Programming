# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:12:17 2019

@author: Alunos
"""

s= 'Qual o número a verificar?'
print (s)
n= int( input())

primo = True

for i in range(2,n):
    if ( n%i == 0 ):
        primo = False
        break

if (primo == True):
    print("O número ",n," é primo")

else:
    print("O número ",n," NÃO é primo")