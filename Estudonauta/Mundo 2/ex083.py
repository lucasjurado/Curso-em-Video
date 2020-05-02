print('='*30)
print('{:^30}'.format('BANCO ITAÚ'))
print('='*30)
valor = int(input('Qual o valor que você quer sacar? R$ '))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de \033[36m{total_ced} cédulas\033[m de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('='*30)