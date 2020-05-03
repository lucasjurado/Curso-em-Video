i = int(input('Digite o termo inicial: '))
n = int(input('Digite o nº de termos: '))
pa = int(input('Digite a razão da PA: '))
c = 1
nv = 1

while nv!=0:
    n = n + nv
    while c< n:
        print(i, end='->')
        i = i + pa
        c = c + 1
    print('PAUSA')
    nv = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {n-1} termos mostrados')