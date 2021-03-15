from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if passo < 0 :
        passo = passo * (-1)
    if passo == 0:
        passo = 1
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c}', end = ' ')
            sleep(0.5)
            c += passo
        print('Fim')
    else:
        c = inicio
        while c >= fim:
            print(f'{c}', end=' ')
            sleep(0.5)
            c -= passo
        print('Fim')
    print('-=' * 20)



contador(1, 10, 1)
contador(10 , 0, 2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
