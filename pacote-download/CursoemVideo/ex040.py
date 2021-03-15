nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print('Sua média foi {}\n=======REPROVADO======='.format(media))
elif 5.0 < media < 6.9:
    print('Sua média foi {}\n=======RECUPERÇÃO======='.format(media))
else:
    print('Sua média foi {}\n=======APROVADO======='.format(media))
