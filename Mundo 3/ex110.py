n = int(input())
lista = []

for c in range (1,n+1):
    vlr = float(f'{(1/c)}')
    if c%2 == 0:
        lista.append(vlr)
    else:
        lista.append(-vlr)

soma = round(sum(lista),6)
print('{:.6f}'.format(soma))