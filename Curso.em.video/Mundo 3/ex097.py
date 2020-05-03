lista = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n%2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    again = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if again in 'N':
        break
print(f'Lista completa: {lista}')
print(f'Lista de itens pares: {lista_par}')
print(f'Lista de itens impares: {lista_impar}')