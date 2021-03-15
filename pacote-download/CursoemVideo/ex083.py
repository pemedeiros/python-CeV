exp = input('Digite uma expressão: ')
abre = exp.count('(')
fecha = exp.count(')')
if abre == fecha:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')