n = int(input())
lista = 0

for c in range (1,n+1):
    vlr = float(f'{(1/(c**2))}')
    lista += float(f'{(1/(c**2))}')


print('{:.6f}'.format(round((lista),6)))