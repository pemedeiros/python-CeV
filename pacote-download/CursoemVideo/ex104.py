def leiaint(msg):
    ok = False
    v = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            v = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor inteiro.\033[m')
        if ok:
            break
    return v


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')