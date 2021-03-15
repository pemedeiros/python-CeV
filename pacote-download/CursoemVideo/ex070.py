total = 0
menor = 999999999
maisd100 = 0
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    opcao = input('Deseja continuar?[S/N]').upper()
    total += preco
    if preco > 1000:
        maisd100 += 1
    if preco < menor:
        barato = nome
    if opcao == 'S':
        print('Insira mais dados')
    elif opcao == 'N':
        print(f'O total foi de R${total}.'
              f'\n{maisd100} produtos custam mais de R$ 1000'
              f'\n{barato} é o nome do produto mais barato.')
        break
