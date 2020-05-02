lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    again = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if again in 'N':
        break

print(f'Foram digitados {len(lista)} valores!')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é: {lista}.')
if 5 in lista:
    print(f'O número 5 está na lista e foi digitado {lista.count(5)} vezes!')
else:
    print('O número 5 não está na lista!')