# Desafio 15
# Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km  rodado.
# Aula 7

km = float(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (0.15 * km) + (60 * dias)
print('Como o carro foi alugado por {} dias e foram percorridos {}km nele, '.format(dias, km), end='')
print('o preço a ser pago é de R${:.2f}.'.format(preco))
