import time
cont_18 = 0
cont_m = 0
cont_f = 0
top_idade = 0
top_idade_sexo = ' '
cnt = 1
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    again = ' '
    while again not in 'SN':
        again = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if idade > 18:
        cont_18 += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade < 20:
        cont_f += 1
    if cnt == 1:
        top_idade = idade
        top_idade_sexo = sexo
    if idade > top_idade:
        top_idade = idade
        top_idade_sexo = sexo
    if again == 'N':
        break
    cnt +=1
print('Processando...')
time.sleep(0.5)
print(f'''Total de pessoas com mais de 18 anos: {cont_18}.
Ao todo temos {cont_m} homens cadastrados.
Temos {cont_f} mulheres com menos de 20 anos.
E a pessoa mais velha é do sexo {top_idade_sexo} e tem {top_idade} anos.''')
