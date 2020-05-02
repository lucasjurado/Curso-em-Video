import datetime
nsc = int(input('Ano do nascimento: '))
ano = datetime.date.today().year
idade = ano - nsc

print(f'Quem nasceu em {nsc} tem {idade} anos atualmente.')
if idade > 18:
    print('Você já deveria ter se alistado há {} anos.\n'
          'Seu alistamento foi em {}.'.format(idade-18, nsc+18 ))
elif idade == 18:
    print('Você deve se alistar neste ano!')
else:
    print('Você deverá se alistar daqui {} anos.\n'
          'Seu alistamento será em {}.'.format(18 - idade, nsc+18))