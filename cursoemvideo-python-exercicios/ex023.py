# Desafio 23
# Faça um programa que leia um nº de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex: Digite um número: 1833
# unidade: 3
# dezena: 3
# centena: 8
# milhar: 1
# Fazer como str e matematicamente
# Aula 9

'''
unidade = 1
dezena = 10 (a parte inteira de qualquer nº/10) x // y
centena = 100 (a parte inteira de qualquer nº/100)
milhar = 1000 (a parte inteira de qualquer nº/1000)

'''

#STR

num = input('Digite um número de 0 a 9999: ')
print('Unidade: {}.'.format(num[3]))
print('Dezena: {}.'.format(num[2]))
print('Centena: {}.'.format(num[1]))
print('Milhar: {}.'.format(num[0]))

#MATH

num = int(input('Digite um número de 0 a 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}:'.format(num))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
