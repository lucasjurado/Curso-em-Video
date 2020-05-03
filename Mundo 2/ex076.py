s = num = c = 0
again = 's'
lista = []
while again in 'Ss':
    num = int(input('Digite um número: '))
    again = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    s += num
    c += 1
    lista = lista + [num]
media = s/c
print(f'Você digitou {c} números e a média foi de {media:.2f}.')
print(f'O maior valor foi {max(lista)} e o menor {min(lista)}.')
