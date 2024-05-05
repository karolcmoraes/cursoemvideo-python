'''
Desafio 30

Crie um programa que leia um numero inteiro qualquer e
mostre na tela se ele é par ou ímpar.

# Aula 10
'''

num = int(input('Digite um número qualquer: '))
if num % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é impar.'.format(num))
