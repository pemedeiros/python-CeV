times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'RB Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 primeiros colocados foram: {times[:5]}')
print(f'Os últimos 4 colocados foram: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
pos = int(times.index('São Paulo'))
print(f'O São Paulo está na posição: {pos + 1}')