total = 0
for c in range(1, 8):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        total += 1
    if total == 0:
        print('Ningúem é maior de idade')
print('{} pessoas são maiores de idade'.format(total))
