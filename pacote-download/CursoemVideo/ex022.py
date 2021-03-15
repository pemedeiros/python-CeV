nome = input('Qual seu nome inteiro?')
print('Seu nome com letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é: {}'.format(nome.lower()))
nd = nome.split()
print('Total de letras:{}'.format(len("".join(nd))))
print('Seu primeiro nome tem {} letras'.format(len(nd[0])))

