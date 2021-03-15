stats = {}
gols = []
tot = 0
stats['nome'] = input('Nome do jogador: ')
stats['partidas'] = int(input(f'Quantas partidas {stats["nome"]} jogou? '))
for c in range(1, stats['partidas'] + 1):
    gols.append(int(input(f'Quanto gols na partida {c}?')))
    stats['gols'] = gols[:]
    tot += gols[c - 1]
    stats['total'] = tot
print(f'O jogador {stats["nome"]} jogou {stats["partidas"]} partidas')
for i, k in enumerate(gols):
    print(f'Na partida {i + 1}, fez {k} gols')
