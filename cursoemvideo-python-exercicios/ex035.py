'''
Desafio 35

Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se eles podem ou não formar um triângulo.

Tem um principio matematico que rege a formação de triangulo. PESQUISAR

Dado um triângulo cujos segmentos medem a, b e c, esse triângulo somente existirá se:
b + c > a
a + c > b
a + b > c

# Aula 10
'''

r1 = float(input('Digite o tamanho da reta 1 em cm: '))
r2 = float(input('Digite o tamanho da reta 2 em cm: '))
r3 = float(input('Digite o tamanho da reta 3 em cm: '))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('Essas retas podem formar um triângulo.')
else:
    print('As retas não formam um triângulo.')
