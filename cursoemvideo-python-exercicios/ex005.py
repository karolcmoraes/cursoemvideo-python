# Desafio 5
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
# Aula 7

# sucessor = x + 1. antecessor = x - 1

ni = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {} e seu sucessor é {}.'. format(ni, (ni-1), (ni+1)))
