from datetime import date

cad = {}
cad['Nome'] = str(input('Nome: '))
nsc = int(input('Ano de Nascimento: '))
cad['Idade'] = (date.today().year - nsc)
cad['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cad['Ctps'] != 0:
    cad['Contratação'] = int(input('Ano da contratação: '))
    cad['Salário'] = float(input('Salário: R$ '))
    cad['Aposentadoria'] = cad['Contratação'] - nsc + 35
print('-=-'*20)

for k,v in cad.items():
    print(f'- {k} tem o valor {v}')