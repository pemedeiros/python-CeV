lista = []
par = []
impar = []
while True:
    n = int(input('Digite o valor: '))
    opcao = input('Deseja continuar?[S/N]').upper()
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if opcao == 'S':
        print('Continuando...')
    if opcao == 'N':
        print(f'A lista geral é {lista}'
              f'\nA lista dos pares é {par}'
              f'\nA lista dos impares é {impar}')