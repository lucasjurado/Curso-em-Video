def quebra():
    print('-'*20)
def area(larg, comp):
    a = larg*comp
    print(f'A área do terreno {larg} x {comp} é de {a}m².')


print('Controle de Terrenos')
quebra()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
