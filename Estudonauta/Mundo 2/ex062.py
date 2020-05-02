cont = 0
num = int(input('Digite um número: '))
for c in range (1,num+1):
    if num % c == 0:
        print('\033[36m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end ='')
print(f'\n\033[mO número {num} foi divisível \033[36m{cont} vezes\033[m!')
if cont == 2:
    print(f'Portanto, o número {num} É PRIMO!')
else:
    print(f'Portanto, o número {num} NÃO É PRIMO!')
