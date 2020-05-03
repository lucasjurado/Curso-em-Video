n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))
lista = (n1,n2,n3)
c = 1
menor = 0
meio = 0
maior = 0

for n in lista:
    if c == 1 or n < menor:
        menor = n
    if c == 1 or n > maior:
        maior = n
    if c == 1 or menor < n < maior:
        meio = n
    c += 1
print('A ordem dos números é {}, {} e {}.'.format(menor,meio,maior))