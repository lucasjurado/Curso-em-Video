p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
med = (p1+p2)/2

if med >= 7:
    print(f'Aprovado! sua média final foi de {med}')
elif med >= 5 and med < 7:
    print(f'Recuperação! sua média final foi de {med}')
elif med < 5:
    print(f'Reprovado! sua média final foi de {med}')