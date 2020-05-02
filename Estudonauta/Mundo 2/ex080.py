import random
print('Vamos jogar PAR ou IMPAR')
cont = 0
while True:
    num = int(input('Digite um valor: '))
    pc = random.randint(0, 10)
    sum = num + pc
    p1 = ' '
    while p1 not in 'PI':
        p1 = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    if sum % 2 == 0:
        resultado = 'Par'
        r = 'P'
    else:
        resultado = 'Impar'
        r = 'I'
    print(f'Você jogou {num} e o pc {pc}. Total de {sum}, deu {resultado}!')
    if p1 == r:
        print('Você venceu! Vamos jogar novamente.')
    else:
        break
    cont += 1
print(f'Você perdeu! Game Over! Você venceu {cont} vezes!')
