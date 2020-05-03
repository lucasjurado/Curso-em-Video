n = int(input())
lista = 0
vlr = 1
c = 1

while ((1/n**2) < vlr):
    vlr = float(f'{(1/(c**2))}')
    lista += float(f'{(1/(c**2))}')
    c += 1

print('{:.6f}'.format(round((lista),6)))