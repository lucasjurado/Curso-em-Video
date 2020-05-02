def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

def soma (a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = soma(3,2,5)
r2 = soma(2,2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2} e {r3}.')
print(f'Os resultados foram {soma(3,2,5)}, {soma(2,2)} e {soma(6)}.')
