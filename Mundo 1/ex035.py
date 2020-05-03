vel=float(input('Qual a velocidade atual do carro? '))
max=80
if vel>80:
    print('Multado! Você excedeu em {} km/h a velocidade máxima de 80km/h \n'
          'Você deve pagar a multa de R${:.2f}!'.format(vel-max, 7*(vel-max)))
print('Tenha um bom dia! Dirija com segurança!')