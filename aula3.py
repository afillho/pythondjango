# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:49:40 2020

@author: Aluno
"""

# Aula 3 18/01/2020  -  Prof. Felipe
# Estruturas de Repetições

"""
x = 2                # Exemplo 1
while x <= 5:                
    print (x)
    x = x + 1
"""

"""
fim = (int(input("Digite o último número: ")))      # Exemplo 2
x = 1
while x <= fim:
    print (x)
    x = x + 1
"""

"""
fim = int(input("Digite o último número: "))      # Exemplo 3
x = 0
while x <= fim:
    if x % 2 != 0:
        print (x)    
    x = x + 1
"""

"""
fim = int(input("Digite o último número: "))      # Exemplo 4
x = 1
a = 1
while x <= fim:
    if x % 3 == 0 and a <= 10:
        print (x)
        a = a + 1
    x = x + 1   
"""

"""
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d número: " %n))      # Exemplo 5
    soma += x                                      # soma = soma + x
    n = n + 1
print ("Soma : %d" %soma)
"""


n = 0
soma = 0
while True:
    x = int(input("Digite o número (0 para sair): "))      # Exemplo 6
    if x == 0:
        break
    else:
        n += 1
    soma += x                                      # soma = soma + x
print ("Média: %5.2f" % (soma/n))


