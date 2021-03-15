maior = 0
menor = 9999999999999
media = 0
med_fim = 0
n = 1
while n != 0:
    num = int(input('Digite um número: '))
    cont = input('Quer continuar?[S/N]').upper()
    media += num
    n += 1
    if cont == 'S':
        print('Continuando...')
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if cont == 'N':
        med_fim = media / (n-1)
        print('A média é {}'.format(med_fim))

        print('O maior número é {} e o menor é {}'.format(maior, menor))

