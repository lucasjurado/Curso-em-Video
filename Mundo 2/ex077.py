n = s = 0
while True:
    n = int(input('Numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')