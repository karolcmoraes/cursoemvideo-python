# Desafio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule e mostre o comprimento da hipotenusa.
# h² = co² + ca²
# Aula 8

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print('O comprimento da hipotenusa é de {:.2f}.'.format(hip))
