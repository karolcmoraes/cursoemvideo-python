'''
Desafio 32

Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Condições para um ano bissexto:
Para ser bissexto, o ano deve ser:

- Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

- Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja,
deixa resto diferente de zero;

- Pode ser que seja divisível por 400. Caso seja divisível por 400,
a divisão deve ser exata, deixando o resto igual a zero.

# Aula 10


ano = int(input('Digite o ano: '))

if ano / 4 == ano // 4 and ano / 100 != ano // 100:
    print('O ano {} é bissexto!'.format(ano))
elif ano / 4 == ano // 4 and ano / 100 == ano // 100 and ano / 400 == ano // 400:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))

'''

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
