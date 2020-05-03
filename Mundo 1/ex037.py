km = float(input('Qual a distância da sua viagem? '))
if km <= 200:
    print('O preço da sua viagem será de R$ {:.2f}!'.format(km*0.5))
else:
    print('O preço da sua viagem será de R$ {:.2f}!'.format(km*0.45))