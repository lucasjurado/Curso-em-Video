import time
print('-'*30)
print('Loja Super Baratão')
print('-'*30)
total = 0
cont_mil = 0
cont_barato = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    again = ' '
    while again not in 'SN':
        again = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('-'*30)
    total += preco
    if preco > 1000:
        cont_mil += 1
    cont_barato += 1
    if cont_barato == 1 or preco < menor_p:
        menor_p = preco
        menor_n = nome
    if again == 'N':
        break
print('Processando...')
time.sleep(1)
print(f'''- - - - - FIM DO PROGRAMA - - - - -
O total da compra foi de R$ {total:.2f}.
Temos {cont_mil} produtos custando mais de R$ 1000.00.
O produto mais barato foi {menor_n} que custa R$ {menor_p:.2f}.''')