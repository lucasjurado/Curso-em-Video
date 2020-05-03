peso = float(input('Seu peso (kg): '))
altura = float(input('Sua altura (m): '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}, considerado ABAIXO DO PESO!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f}, considerado PESO IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f}, considerado SOBREPESO!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f}, considerado OBESIDADE!'.format(imc))
else:
    print('Seu IMC é de {:.2f}, considerado OBESIDADE MORBIDA!'.format(imc))
