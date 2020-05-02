a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))


if a+b > c and a+c > b and b+c > a:
    print('Os segmentos podem formar um triângulo ', end = '')
    if a == b == c:
        print('equilátero')
    elif a == b and c != a or a == c and b != a or b == c and a != b:
        print('isósceles')
    if a != b != c != a:
        print('escaleno')
else:
    print('Os segmentos não podem formar um triângulo!')