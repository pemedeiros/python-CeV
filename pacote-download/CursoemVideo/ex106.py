def ajuda(*comandos):
    print(help(c))


while True:
    print('\033[0;34m~\033[m' * 20)
    c = input('\033[0;34mDigite um comando:\033[m ')
    print('\033[0;34m~\033[m' * 20)
    if c == 'fim':
        print('\033[0;31mAté mais!\033[m')
        break
    else:
        ajuda(c)
