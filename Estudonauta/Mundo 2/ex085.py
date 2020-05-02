print('-----Cordenadas-----')
x = float(input('Digite a coordenada do eixo X (0 - 10.0): '))
y = float(input('Digite a coordenada do eixo Y (0 - 10.0): '))

if x == 0 and y == 0:
    c = 'Origem'
elif x > 0 and y > 0:
    c = 'Q1'
elif x > 0 and y < 0:
    c = 'Q4'
elif x < 0 and y > 0:
    c = 'Q2'
elif x < 0 and y < 0:
    c = 'Q3'
else:
    c = 'No eixo'
print(f'A posição das coordenadas {x} e {y} é {c}')