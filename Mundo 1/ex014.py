print('Vamos calcular a quantidade de tinta necessária para pintar a parede!')
print('-'*25)
l=float(input('Qual é a largura da parede em metros? '))
a=float(input('Qual é a altura da parede em metros? '))
area=(l*a)
t=(0.5*area)
print('Para pintar essa parede de {:.2f} m², então será necessário {:.2f} litros de tinta!'.format(area,t))