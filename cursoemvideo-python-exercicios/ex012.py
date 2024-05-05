# Desafio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Aula 7

p = float(input('Digite o preço: R$'))
print('Com 5% OFF, o produto está saindo a R${:.2f}.'.format((95*p)/100))
