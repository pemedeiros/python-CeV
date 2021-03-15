l1 = float(input('Insira o comprimento do primeiro lado: '))
l2 = float(input('Insira o comprimento do segundo lado: '))
l3 = float(input('Insira o comprimento do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Podem formar um triângulo')
    if l1 == l2 == l3:
        print('Triângulo equilátero')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Não podem formar um triângulo')
