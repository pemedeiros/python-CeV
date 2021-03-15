listagem = ('Pao', 1, 'Arroz', 22.75, 'Peixe', 4)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:>7.2f}')