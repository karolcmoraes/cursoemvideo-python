# Desafio 6
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# Aula 7

n = int(input('Digite um número: '))
print('O dobro de {} é {} e seu triplo é {}. \nA raíz quadrada de {} é {:.2f}.'.format(n, (n*2), (n*3), n, (n**(1/2))))
