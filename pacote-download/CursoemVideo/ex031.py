km = int(input('Qual a distancia em Km para o destino?'))
if km > 200:
    print('O preço da passagem é de R${}'.format(km * 0.45))
else:
    print('O preço da passagem é de R${}'.format(km * 0.50))