def area(larg, compr):
    a = larg * compr
    print(f'A área do seu terreno de {larg} x {compr} é de {a} m².')


l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento terreno em metros: '))
area(l, c)