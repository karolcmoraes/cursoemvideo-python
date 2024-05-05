'''
Desafio 28

Escreva um programa que faça o computador 'pensar' em um nº inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o nº escolhido pelo
computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Aula 10
'''

import random
num = random.randint(0, 5)
while True:
    chute = int(input('Chute um número aleatório entre 0 e 5: '))
    if chute == num:
      print('Parabéns, você acertou!')
      break
    elif chute > num:
        print('Seu chute foi muito alto. Você errou')
    elif chute < num:
        print('Seu chute foi muito baixo. Você errou.')
        continue
