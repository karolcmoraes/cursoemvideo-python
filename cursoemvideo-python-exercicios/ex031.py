'''
Desafio 31

Desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens de
até 200km e R$0.45 para viagens mais longas.

# Aula 10


d = float(input('Qual é a distância da viagem em km? '))
if d <= 200:
    print('O valor da passagem é R${:.2f}.'.format(int(d * 0.50)))
else:
    print('O valor da passagem é R${:.2f}.'.format(int(d * 0.45)))

'''

d = float(input('Qual é a distância da viagem em km? '))
preço = d * 0.50 if d <= 200 else d * 0.45
print('O valor da sua passagem é R${:.2f}'.format(int(preço)))
