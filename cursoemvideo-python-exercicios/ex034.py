'''
Desafio 34

Escreva um programa que calcule o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

# Aula 10
'''

salario = float(input('Qual é o seu salário? '))
if salario > 1250.00:
    print('Com 10% de aumento, seu salário passou a ser R${:.2f}.'.format(salario + (salario * (10/100))))
elif salario <= 1250.00:
    print('Com 15% de aumento, seu salário passou a ser R{:.2f}.'.format((salario + (salario * (15/100)))))
