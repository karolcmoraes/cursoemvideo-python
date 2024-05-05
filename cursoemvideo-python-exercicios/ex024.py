# Desafio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome 'SANTO'.
# Aula 9

city = input('Digite o nome de uma cidade: ')
city = city.title()
city = city.strip()
if city.startswith('Santo'):
    print('A cidade {} começa com o nome Santo.'.format(city))
else:
    print('A cidade {} não começa com o nome Santo.'.format(city))

city = input('Em qual cidade você nasceu? ')
city = city.title()
city = city.strip()
print(city[:5] == 'Santo')
