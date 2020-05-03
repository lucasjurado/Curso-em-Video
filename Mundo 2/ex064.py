import datetime
atual = datetime.date.today().year
cont = 0
for c in range (1,8):
    nasc = int(input(f'{c}º ano de nascimento: '))
    if atual - nasc >= 21:
        cont = cont +1
print(f'O número de pessoas maiores de idade é de {cont}.\n'
      f'Já o número de pessoas menores de idade é de {7-cont}.')