from random import randint
from time import sleep

print('-'*40)
print('{:^40}'.format ('JOGA NA MEGA SENA'))
print('-'*40)

n = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:.^40}'.format (f'SORTEANDO {n} JOGOS'))

lista = []
count = 0
for c in range (0,n):
    sleep(0.3)
    jogo = print(f'Jogo {c+1}: ', end='')
    while True:
        num = (randint(1,60))
        if num not in lista:
            lista.append(num)
            count += 1
        if count == 6:
            break
    lista.sort()
    print(f'{lista}')
    lista.clear()
    count = 0