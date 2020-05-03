num = [[],[]]
for n in range (0,7):
    vlr = int(input(f'Digite o {n+1}º valor: '))
    if vlr%2 == 0:
        num[0].append(vlr)
    else:
        num[1].append(vlr)
print('-=-'*10)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores impares digitados foram: {num[1]}')

