n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tup = (n1,n2,n3,n4)

print(f'Você digitou os números {tup}.')
print(f'O número 9 apareceu {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O valor 3 apareceu pela 1ª vez na {tup.index(3) + 1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados foram: ', end ='')
for p in tup:
    if p%2 == 0:
        print(f'{p}', end=', ')