# Desafio 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar.
# Considere US$1,00 = R$3,27
# Aula 7

d = float(input('Quantos reais você tem? R$'))
print('Com R${:.2f} reais você pode comprar US${:.2f} doláres.'.format(d, (d/3.27)))
