n = int(input('Digite um número: '))
print(f'A tabuada do número \033[34m{n}\033[m é:')
for c in range (1,11):
     print(f'\033[34m{n}\033[m x {c} =', c*n)
