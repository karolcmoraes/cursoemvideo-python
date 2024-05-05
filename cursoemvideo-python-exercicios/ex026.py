# Desafio 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.
# Aula 9

letra = input('Digite uma frase: ')
letra = letra.lower()
letra = letra.strip()
print('A letra A aparece {} vezes.'.format(letra.count('a')))
print('A letra A aparece na posição {} a 1ª vez.'.format((letra.find('a')) + 1))
print('A letra A aparece na posição {} a última vez.'.format((letra.rfind('a')) + 1))
