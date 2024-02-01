# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int( input('Introduza um número inteiro:') )
m = int( input('Introduza outro número inteiro maior:') )

soma = 0

if( n < m ):
    for i in range(n,m+1):
        if( i%2 == 0):
            soma = soma + i
            #print(soma) 
        else:
            continue
    print('A soma de todos os números pares entre ',n,' e ',m,' dá:',soma)
    
else:
    print('Erro - o 1º número é maior do que o 2º!')