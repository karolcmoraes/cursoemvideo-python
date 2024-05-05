# Desafio 4
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ela.
# Aula 6

info = input('Digite algo: ')
print('{} é uma {}'.format(info, type(info)))
print('{} é alphanumérico: '.format(info), info.isalnum())
print('{} é alpha: '.format(info), info.isalpha())
print('{} é numérico: '.format(info), info.isnumeric())
print('{} só tem espaços: '.format(info), info.isspace())
print('{} está em maiúsculas: '.format(info), info.isupper())
print('{} está em minúsculas: '.format(info), info.islower())
print('{} está capitalizada: '.format(info), info.istitle())
