num = ('zero','um','dois','três','quarto','cinco','seis','sete','oito','nove','dez')

while True:
    n = -1
    while n <0 or n>10:
        n = int(input('Digite um número entre 0 e 10: '))
        if n <0 or n>10:
            print(f'O valor digitado: {n}, não pertence ao intervalo! Tente novamente.')
    if 0 <= n <= 10:
        print(f'Você digitou o número {num[n]}.')
    again = ' '
    while again not in 'SN':
        again = str(input('Quer continuar? ')).upper().strip()[0]
    if again == 'N':
        break
print('Fim do programa!')



