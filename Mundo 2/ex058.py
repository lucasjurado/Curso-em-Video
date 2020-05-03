i = int(input('Início do intervalo: '))
f = int(input('Fim do intervalo: '))
esc = str(input('impares (imp) ou pares (par)? '))
mult = int(input('Multiplo de qual número? '))

soma = 0
cont = 0

for c in range (mult,f+1,mult):
    if esc == 'par' and c%mult == 0 and c%2 == 0:
        print (c, end = ' ')
        soma = soma + c
        cont = cont + 1
    elif esc == 'imp' and c%mult == 0 and c%2 == 1:
        print (c, end = ' ')
        soma = soma + c
        cont = cont + 1
    elif esc == 'imp' and c%2 == 0:
        print('', end = '')

print('A soma de todos os {} valores é {}!'.format(cont,soma))

