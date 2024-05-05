# Desafio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.
# Aula 9

nome = input('Digite o nome completo: ')
nome = nome.strip()
nome = nome.title()
if 'Silva' in nome:
    print('{} tem Silva no nome.'.format(nome))
else:
    print('{} não tem Silva no nome.'.format(nome))

nome = input('Qual é o seu nome completo? ')
nome = nome.strip()
nome = nome.title()
print('Seu nome tem Silva? {}.'.format('Silva' in nome))
