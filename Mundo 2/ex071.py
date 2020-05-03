num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
fat = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end ='')
    print(' x ' if cont > 1 else ' = ', end = '')
    fat = fat * cont
    cont -= 1
print(f'{fat}')

#for cont in range (num,0,-1):
#    print(f'{cont}', end ='')
#    print(' x ' if cont > 1 else ' = ', end ='')
#    fat = fat * cont
#print(f'{fat}')
