import math
ang=float(input('Digite o valor de um ângulo: '))
rd=math.radians(ang)
sin=math.sin(rd)
cos=math.cos(rd)
tg=math.tan(rd)
print('O valor do seno do ângulo de {}° é {:.2f}\n'
      'Já o valor do cosseno é {:.2f}\n'
      'Por fim, o valor da tangente é {:.2f}.'.format(ang,sin,cos,tg))
