def leiaDin(msg):
    ok = False
    v = 0
    while True:
        p = str(input(msg))
        if p.isnumeric():
            v = int(p)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM VALOR VÁLIDO.\033[m')
        if ok:
            break
    return v