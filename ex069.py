maiores = h = m = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa[M/F]: ').upper()
    opcao = input('Deseja continuar?[S/N]').upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        h += 1
    if idade < 20 and sexo == 'F':
        m += 1
    if opcao == 'S':
        print('Insira mais dados')
    elif opcao == 'N':
        print(f'{maiores} pessoas tem mais de 18 anos'
              f'\n{h} homens foram cadastrados'
              f'\n{m} mulheres menores de 20 anos foram cadastradas.')
        break
