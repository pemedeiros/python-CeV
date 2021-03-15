def leiaint(msg):
    while True:
        try:
            v = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro.\033[m')
            continue
        else:
            return v


def leiafloat(msg):
    while True:
        try:
            v = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor real.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o valor.\033[m')
            v = 0
            continue
        else:
            return v


num = leiaint('Digite um número inteiro: ')
fl = leiafloat('Digite um número real: ')
print(f'O número inteiro foi {num} e o real foi {fl}')