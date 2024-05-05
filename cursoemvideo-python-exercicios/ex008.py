# Desafio 8
# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.
# km hm dm m dm cm mm
# Aula 7

m = float(input('Digite a quantidade em metros: '))
print('{:.2f}m é igual a {:.2f}cm e {:.2f}mm.'.format(m, (m*100), (m*1000)))
