# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:58:34 2019

@author: Aluno
"""

# idade = 12
# nome = 'Antonio Filho'

# idade = input ("Digite sua idade: ")
# nome = input ("Digite seu nome: ")

idade = int(input ("Digite sua idade: "))
#nome = input ("Digite seu nome: ")

#print (f" Olá {nome}\n sua idade são {idade} anos!")

if idade >= 18:
    print (f"Eleitor de maior idade: {idade} anos!")
elif idade >=16 and idade < 18:
    print (f"Eleitor de menor idade: {idade} anos!")
else:
    print (f"Ainda não é elitor: {idade} anos!")
    

