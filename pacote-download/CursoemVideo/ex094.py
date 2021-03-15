geral = []
pessoa = {}
mulher = []
acima = []
totpessoas = media = idadetot = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo[M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    opcao = input('Deseja continuar?[S/N]').upper()
    if pessoa['sexo'] == 'F':
        mulher.append(pessoa['nome'])
    geral.append(pessoa.copy())
    totpessoas += 1
    idadetot += pessoa['idade']
    media = idadetot / totpessoas
    if pessoa['idade'] > media:
        acima.append(pessoa['nome'])
    if opcao == 'N':
        print(f'Você cadastrou {totpessoas} pessoas.')
        print(f'A média de idade do grupo é de {media} anos.')
        print(f'As mulheres cadastradas foram: {mulher}')
        print(f'As pessoas que estão acima da média de idade são: {acima}')
        break


