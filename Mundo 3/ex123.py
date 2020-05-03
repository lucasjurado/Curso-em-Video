def leia(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[31mErro! Digite um nº inteiro válido.\033[m')


num = leia('Digite um número: ')
print(f'Você digitou o número {num}.')

