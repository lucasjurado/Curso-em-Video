lista = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O valor {n} foi adicionado ao final da lista')
    else:
        for p in range (0, len(lista)):
            if n < lista[p]:
                lista.insert(p,n)
                print(f'O valor {n} foi adicionado na posição {p}!')
                break
print(f'Os valores em ordem crescente são: {lista}.')