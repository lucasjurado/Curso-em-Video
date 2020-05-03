import time
import random
print('Vamos jogar Jokenpô!!!')
nome = str(input('Qual é o seu nome? '))
num = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? '''))

if num != 0 and num != 1 and num != 2:
    print('\033[31mOpção inválida!\033[m')
    exit()
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!!!')
time.sleep(0.5)

print('-='*20)

lista = ('Pedra','Papel','Tesoura')
pc = random.choice(lista)
p1 = lista[num]

print(f'Computador escolheu \033[34m{pc}\033[m!')
print(f'{nome} escolheu \033[35m{p1}\033[m!')

print('-='*20)

if pc == p1:
    print('\033[36mEmpate!!!\033[m')
elif pc == 'Pedra' and p1 == 'Papel' or pc == 'Papel' and p1 == 'Tesoura' or pc == 'Tesoura' and p1 == 'Pedra':
    print(f'\033[32m{nome}, você venceu!!!\033[m')
else:
    print(f'\033[31m{nome}, você perdeu!!!\033[m')
