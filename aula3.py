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

"""
funcionarios = [
        [1, "José", "00h00"],
        [2, "José", "00h10"],
        [3, "José", "00h30"],
        [4, "José", "00h00"],
        [5, "José", "01h00"],
        [6, "José", "00h10"],
        [7, "José", "01h00"],
        [8, "José", "00h00"],
        [9, "José", "01h00"],
        [10, "José", "01h10"],
        [11, "José", "00h00"],
        [12, "José", "01h10"],
        ]

horarios = []
x= 0
h1=h2=h3=h4=h5=h6=h7=h8=h9=h10=h11=h12 = 0

h = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12]

for f in funcionarios:
    if not f[2] in horarios:
        horarios.append(f[2])
    h[x] += 1
    print(h)    
        
        
horarios.sort()

for x in horarios:
    print(x, h)    
"""
 


t = [-10, -8, 0, 1, 2, 5, -2, -4]

a = b = m = 0

for x in t:
    if x <= a:
        a = x
    elif x >= b:
        b = x
    m += x
            
    
print("Mais baixa: %f Mais alta: %f Média: %f" % (a, b, m/len(t)))
    
    
    
"""
for f in funcionarios:
    if not f[2] in horarios:
        horarios.append(f[2])
    h[x] += 1
    print(h)    
        
        
horarios.sort()

for x in horarios:
    print(x, h) 
"""
        
        
 