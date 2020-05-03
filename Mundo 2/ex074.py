print('Sequência de Fibonacci')
print('-'*35)
n = int(input('Quantos termos você quer mostrar? '))
i1 = 0
i2 = 1
print(f'{i1} -> {i2} -> ', end = '')
cont = 3
while cont <= n:
    i3 = i1 + i2
    print(f'{i3}', end = ' -> ')
    i1 = i2
    i2 = i3
    cont += 1
print('Fim')
print(f'A soma de todos os \033[36m{n}\033[m primeiros termos na Sequência de Fibonacci é igual a \033[36m{i1+i2+i3}\033[m!')