maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa : KG'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} KG'.format(maior))
print('O menor peso foi {} KG'.format(menor))