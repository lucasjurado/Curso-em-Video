mt = [[0,0,0], [0,0,0], [0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        mt[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-='*10)
for l in range (0,3):
    for c in range (0,3):
        print(f'[ {mt[l][c]:5^} ]', end ='')
    print()
print('=-=' * 10)

par = []
tc = []
maior = []
for l in range (0,3):
    for c in range (0,3):
        if mt[l][c] % 2 == 0:
            par.append(mt[l][c])
        if c == 2:
            tc.append(mt[l][c])
        if l == 1:
            maior.append(mt[l][c])

print(f'A soma dos valores pares é: {sum(par)}.')
print(f'A soma dos valores da terceira coluna é: {sum(tc)}.')
print(f'O maior valor da segunda linha é: {max(maior)}.')