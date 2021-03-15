dado = []
pessoas = []
maior = c = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    c += 1
    if c == 1:
        maior = menor = dado[1]
    else:
        if dado[1] >= maior:
            maior = dado[1]
        if dado[1] <= menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    print(pessoas)

    opcao = input('Deseja continuar?[S/N]').upper()
    if opcao == 'S':
        print('Continuando...')


    if opcao == 'N':
        print(f'Você cadastrou {c} pessoas')
        print(f'\nO maior peso foi de {maior} Kg. Peso de', end = '' )
        for p in pessoas:
            if p[1] == maior:
                print(p[0])
        print(f'\nO menor peso foi de {menor} Kg. Peso de', end = '')
        for p in pessoas:
            if p[1] == menor:
                print(p[0])
        break

