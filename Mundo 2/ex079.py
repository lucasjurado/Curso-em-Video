while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x \033[36m{c}\033[m = {n*c}')
print('Programa de tabuada encerrado!')