from time import sleep

def contador (i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if f > i:
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    elif f < i:
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    else:
        print('Erro! Início é igual ao fim.')

def quebra():
    print('-'*30)

contador(1,10,1)
quebra()
contador(10,0,-1)
quebra()

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
quebra()
contador(i,f,p)
quebra()
