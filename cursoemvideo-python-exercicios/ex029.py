'''
Desafio 29

Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custa R$7,00 por cada km acima do limite.

# Aula 10
'''

v = float(input('Digite a velocidade em km/h: '))
if v > 80:
    print('Você foi multado.')
    print('Sua multa vai custar: R${:.2f}.'.format(int((v - 80) * 7)))
else:
    print('Você está dentro do limite de velocidade.')
