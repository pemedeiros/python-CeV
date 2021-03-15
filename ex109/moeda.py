def aumentar(n=0, porcent=0, formatado=False):
    final = n + (n * (porcent / 100))
    return final if formatado is False else moeda(n)


def diminuir(n=0, porcent=0, formatado=False):
    final = n - (n * (porcent / 100))
    return final if formatado is False else moeda(final)


def dobro(n=0, formatado=False):
    final = n * 2
    return final if formatado is False else moeda(final)


def metade(n=0, formatado=False):
    final = n / 2
    return final if formatado is False else moeda(final)


def moeda(n=0, moeda ='R$', format=False):
    return f'{moeda}{n:>8.2f}'.replace('.',',')