cad = {}

cad['Nome'] = str(input('Nome: '))
cad['Média'] = float(input(f'Média de {cad["Nome"]}: '))
if cad['Média'] >= 6:
    cad['Situação'] = 'Aprovado'
elif 6 > cad['Média'] >= 5:
    cad['Situação'] = 'Recuperação'
else:
    cad['Situação'] = 'Reprovado'

for k,v in cad.items():
    print(f'{k} é igual a {v}.')
