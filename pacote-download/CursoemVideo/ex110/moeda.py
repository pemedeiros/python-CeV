def aumentar(n=0, porcent=0, formatado=False):
    final = n + (n * (porcent / 100))
    return final if formatado is False else moeda(final)


def diminuir(n=0, porcent=0, formatado=False):
    final = n - (n * (porcent / 100))
    return final if formatado is False else moeda(final)


def dobro(n=0, formatado=False):
    final = n * 2
    return final if formatado is False else moeda(final)


def metade(n=0, formatado=False):
    final = n / 2
    return final if formatado is False else moeda(final)


def moeda(n=0, moeda ='R$'):
    return f'{moeda}{n:>8.2f}'.replace('.',',')


def resumo(n=0, aum=0, red=0):
    print('-'*20)
    print('       RESUMO')
    print('-'*20)
    print(f'Preço analisado: {moeda(n)}')
    print(f'Metade do preço: {metade(n, True)}')
    print(f'Dobro do preço:  {dobro(n, True)}')
    print(f'Aumentando 80%:  {aumentar(n, aum, True)}')
    print(f'Reduzindo 35%:   {diminuir(n, red, True)}')