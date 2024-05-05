# Desafio 14
# Escreva um programa que converta uma temperatura difitada em ºC para ºF.
# Aula 7

# ºF = (ºC x 1,8) + 32

c = float(input('Informe a temperatura em ºC: '))
f = (c * 1.8) + 32
print('A temperatura de {}ºC corresponde a uma de {}ºF.'.format(c, f))
