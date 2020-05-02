listanum = []

while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print(f'Valor {n} foi adicionado com sucesso!')
    else:
        print(f'{n} é duplicado! Não será adicionado...')

    again = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if again in 'N':
        break

listanum.sort()
print(f'Os valores adicionados foram: {listanum}.')