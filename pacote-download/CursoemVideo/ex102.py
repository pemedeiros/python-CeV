def fatorial(num, show = False):
    from math import factorial
    fat = factorial(num)
    if show == False:
        print(fat)
    else:
        c = num
        f = 1
        while c > 0:
            print(f'{c}', end='')
            print(f' x ' if c > 1 else ' = ', end= ' ')
            f *= c
            c -= 1
        print(fat)

fatorial(5, True)