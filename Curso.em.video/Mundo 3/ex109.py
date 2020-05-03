pessoa = {}
grupo = []
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    grupo.append(pessoa.copy())

    while True:
        again = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if again in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if again == 'N':
        break
print('-'*20)

print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma/len(grupo):.2f} anos.')
print('C) As mulheres cadastradas foram: ', end="")

for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print()

print('D) Lista das pessoas que tem idade acima da média:')
for p in grupo:
    if p['idade'] > soma/len(grupo):
        for k, v in p.items():
            print(f' {k} = {v}; ', end='')
        print()
print('Fim do Programa!')
