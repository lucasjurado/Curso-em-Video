preco = float(input('Qual o preço do produto? R$ '))
fp = (input('''Qual será a forma de pagamento? 
    a) à vista dinheiro/cheque;
    b) à vista no cartão de crédito;
    c) 2x no cartão de crédito;
    d) 3x ou + no cartão de crédito.
Digite a opção: '''))
if fp == "a" or fp == "a)":
    print(f'O valor a pagar será de R$ {0.9*preco:.2f}')
elif fp == 'b' or fp == 'b)':
    print(f'O valor a pagar será de R$ {0.95*preco:.2f}')
elif fp == 'c' or fp == 'c)':
    print(f'O valor a pagar será de R$ {preco:.2f}. 2 parcelas de R$ {preco/2:.2f}!')
elif fp == 'd' or fp == 'd)':
    parc = int(input('Qual o número de parcelas? '))
    print(f'O valor total a pagar será de R$ {1.2 * preco:.2f}. {parc} parcelas de R$ {(1.2*preco)/parc:.2f}!')
else:
    print('Opção inválida!')
