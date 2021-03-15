def notas(*notas, situacao = False):
    dic = {}
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['media'] = sum(notas) / len(notas)
    if situacao:
        if dic['media'] >= 6:
            dic['situação'] = 'Aprovado'
        else:
            dic['situação'] = 'Reprovado'
    return dic


resp = notas(5.5, 9.5, 10, 6.5, situacao = True)
print(resp)
