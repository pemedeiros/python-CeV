from random import randint
from time import sleep
from operator import itemgetter
'''num = {}
for c in range(1, 5):
    num['jogador'] = 'Jogador'
    num['numero'] = randint(1,6)
    for k, v in num.items():
        print(f'O {k} é {v}', end = ' ')'''
num = {
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)
}
ranking = []
for k, v in num.items():
        print(f'O {k} tirou {v}', end = ' ')
        print()
        sleep(1)
ranking = sorted(num.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)

