lista = []
c = 0
while True:
    n = int(input('Digite o valor: '))
    lista.append(n)
    c += 1
    opcao = input('Deseja continuar?[S/N]').upper()
    if opcao == 'S':
        print('Continuando...')
    if opcao == 'N':
        print(f'Você digitou {c} elementos')
        lista.sort(reverse = True)
        print(f'Os valores em ordem decrescente são {lista}')
        if 5 in lista:
            print('O valor 5 faz parte dessa lista')
        else:
            print('O valor 5 não faz parte dessa lista')
        break