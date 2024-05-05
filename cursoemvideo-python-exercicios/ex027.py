# Desafio 27
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza
# Aula 9

nome = input('Digite o nome completo: ')
nome = nome.title()
nome = nome.strip()
print('Nome: {}.'.format(nome))
nome = nome.split()
primeiro = nome[0]
ultimo = nome[-1]
print('Primeiro nome: {}.'.format(primeiro))
print('Último nome: {}.'.format(ultimo))

n = str(input('Digite seu nome completo: ')).strip()
n = n.title()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
