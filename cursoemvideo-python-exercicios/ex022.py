# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Quantas letras ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome
# Aula 9

nome = str(input('Digite o nome completo: '))
print('Nome em maiúsculo: {}.'.format(nome.upper()))
print('Nome em minúsculo: {}.'.format(nome.lower()))
junto = nome.replace(' ', '')
print('O nome {} tem {} letras.'.format(nome, len(junto)))
primeiro = nome.split()
print('O primeiro nome tem {} letras.'.format(len(primeiro[0])))
