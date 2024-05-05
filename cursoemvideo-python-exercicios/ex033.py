'''
Desafio 33

Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

# Aula 10

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 < n2 and n2 < n3:
    print('O menor número é: {}.'.format(n1))
    print('O maior número é: {}.'.format(n3))
elif n1 < n3 and n3 < n2:
    print('O menor número é: {}.'.format(n1))
    print('O maior número é: {}.'.format(n2))
elif n2 < n1 and n1 < n3:
    print('O menor número é: {}.'.format(n2))
    print('O maior número é: {}.'.format(n3))
elif n2 < n3 and n3 < n1:
    print('O menor número é: {}.'.format(n2))
    print('O maior número é: {}.'.format(n1))
elif n3 < n1 and n1 < n2:
    print('O menor número é: {}.'.format(n3))
    print('O maior número é: {}.'.format(n2))
elif n3 < n2 and n2 < n1:
    print('O menor número é: {}.'.format(n3))
    print('O maior número é: {}.'.format(n1))

'''

a1 = int(input('Digite o 1º número: '))
a2 = int(input('Digite o 2º número: '))
a3 = int(input('Digite o 3º número: '))

maior = a1
if a2 > a1 and a2 > a3:
    maior = a2
elif a3 > a1 and a3 > a2:
    maior = a3
print('O maior núméro é {}.'.format(maior))
menor = a1
if a2 < a1 and a2 < a3:
    menor = a2
elif a3 < a1 and a3 < a2:
    menor = a3
print('O menor número é {}.'.format(menor))
