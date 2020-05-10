print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

tup = ('Lápis', 1.75,
       'Borracha', 2.00,
       'Caderno', 15.00,
       'Estojo', 25.00,
       'Transferidor', 4.20,
       'Compasso', 9.99,
       'Mochila', 120.32,
       'Canetas', 22.30,
       'Livro', 34.90)

n = 0
for i in tup:
    while n<18:
        print(f'{tup[n]:.<30}R$ {tup[n+1]:>6.2f}')
        n += 2
print('-' * 40)