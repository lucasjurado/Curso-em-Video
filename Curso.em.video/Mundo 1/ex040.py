salario = float(input('Digite o valor do salário R$ '))
'''new1 = salario * 1.15
new2 = salario * 1.10
if salario <= 1250:
    print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {new1:.2f} agora.')
else:
    print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {new2:.2f} agora.')'''

if salario <= 1250:
    novo = salario * 1.15
if salario > 1250 and salario <= 5000:
    novo = salario * 1.10
if salario > 5000:
    novo = salario * 1.05
print(f'O novo salario será de R$ {novo:.2f}.')