i = int(input('Digite o termo inicial: '))
n = int(input('Digite o número de termos: '))
pa = int(input('Digite a razão da PA: '))
for c in range (i, i+(n*pa), pa):
    print(c, end =' -> ')
print('Fim')