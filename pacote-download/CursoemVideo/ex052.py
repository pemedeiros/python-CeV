num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = ' ')
        total += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end = ' ')
if total == 2:
    print('\nO número {} é PRIMO'.format(num))
else:
    print('\nO número {} NÃO É PRIMO'.format(num))
