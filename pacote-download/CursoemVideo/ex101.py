def voto(idade):
    from datetime import date
    ano_int = date.today().year
    anos = ano_int - idade
    if anos < 16:
        return f'Com {anos}: O VOTO É NEGADO'
    elif 16 <= anos < 18 or anos > 65:
        return f'Com {anos}: O VOTO É OPCIONAL  '
    else:
        return f'Com {anos}: O VOTO É OBRIGATÓRIO'


nasc = int(input('Que ano você nasceu?'))
print(voto(nasc))