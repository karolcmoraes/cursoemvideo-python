# Desafio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário com 15% de aumento.
# Aula 7

salario = float(input('Digite o seu salário atual: R$'))
print('Com aumento de 15%, seu salário agora será de R${:.2f}.'.format((115*salario)/100))
