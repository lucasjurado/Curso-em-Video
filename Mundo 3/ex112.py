n = int(input())
x = int(input())
lista = []
acum = 0
c = 1

while True:
    s = (c * n)
    if s >= x:
        break
    acum += 1
    c += 1
    lista.append(s)

print(f'O numero {n} tem {acum} multiplos menores que {x}.')