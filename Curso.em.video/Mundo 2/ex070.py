import time
n1=float(input('Primeiro valor: '))
n2=float(input('Segundo valor: '))
lista =[n1,n2]
opc = 0
while opc != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opc = int(input('>> Qual é a sua opção? '))
    print('Processando...')
    time.sleep(0.5)
    if opc == 1:
        print(f'A \033[36msoma\033[m é igual a {n1+n2:.1f}. Gostaria de saber outra informação? ')
    elif opc == 2:
        print(f'A \033[36mmultiplicação\033[m é igual a {(n1*n2):.1f}. Gostaria de saber outra informação? ')
    elif opc == 3:
        print(f'O \033[36mmaior valor\033[m digitado foi o {max(lista):.1f}. Gostaria de saber outra informação? ')
    elif opc == 4:
        print('\033[32mNovos valores!\033[m')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
        time.sleep(1)
    else:
        opc = int(input('\033[31mOpção inválida!\033[m Digite novamente sua opção: '))
print('\033[31mFim do programa!')