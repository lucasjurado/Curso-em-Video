def notas(*vlr,sit = False):
    r = {}
    r['total'] = len(vlr)
    r['maior'] = max(vlr)
    r['menor'] = min(vlr)
    r['média'] = sum(vlr)/(len(vlr))
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r

print(notas(8,9,6,9, sit = True))