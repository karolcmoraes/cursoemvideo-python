# Desafio 16
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6.
# funções do modulo math
# Aula 8

import math
num = float(input('Digite um número: '))
resul = math.trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, resul))

from math import trunc
num = float(input('Digite um número: '))
resul = trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, resul))
