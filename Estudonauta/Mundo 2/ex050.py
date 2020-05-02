import datetime
ano = int(input('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano

print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print('Mirim')
elif 9 < idade <=14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master')