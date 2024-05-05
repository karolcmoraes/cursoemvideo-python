# Desafio 18
# Faça um programa que leia um angulo qualquer e mostre na tela
# o valor do seu seno, cosseno e tangente desse angulo.
# Aula 8

import math
a = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('Sendo o ângulo {}, o seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(a, sen, cos, tg))
