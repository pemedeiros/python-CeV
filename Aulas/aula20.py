'''def linha():
    print('-' * 30)


linha()
print('Curso em vídeo')
linha()
linha()
print('Aprenda Python')
linha()'''

'''
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('PEDRO AUGUSTO')'''
'''def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(1, 3)'''
'''def contador(*num):
    print(num)
    print(len(num))


contador(5, 4, 3, 2, 3, 6)
contador(4)'''
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 4, 5, 2]
dobra(valores)
print(valores)
