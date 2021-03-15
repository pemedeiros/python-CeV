km = int(input('Qual a velocidade do carro em Km/H?'))
if km > 80:
    qtd = km - 80
    multa = qtd * 7
    print('Você foi multado, seu carro estava a {} Km/h além do permitido(80Km/H), o valor da multa é de R${}.'.format(qtd, multa))
else:
    print('Você respeitou as leis de trânsito!')