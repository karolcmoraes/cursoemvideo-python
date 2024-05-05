# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro da tinta pinta uma área de 2m**2.
# Aula 7

l = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))
a = l*h
v = a/2
print('Sendo a largura {:.2f} e altura {:.2f}, a área é de {:.2f}m².'.format(l, h, a))
print('Portanto, para pintar a parede precisa de {:.2f}L de tinta.'.format(v))