lista = []
while True:
    val = int(input('Digite o valor: '))
    if val not in lista:
        lista.append(val)
        print('Valor adicionado')
    else:
        print('Valor não adicionado')
    opcao = input('Deseja continuar?[S/N]').upper()
    if opcao == 'S':
        print('Continuando...')
    if opcao == 'N':
        break
lista.sort()
print(f'Você escolheu os valores {lista}')
