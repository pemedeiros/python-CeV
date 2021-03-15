def ficha(nome = '', gols = 0):
    if g == '':
        gols = 0
    if n == '':
        nome = '<desconhecido>'
    print(f'Nome: {nome}'
          f'\nGols: {gols}')


n = input('Nome:')
g = input('Gols:')
ficha(n, g)