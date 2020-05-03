print('Vamos calcular o valor da hipotenusa de um triângulo retângulo!')
print('-'*35)
import math
ca = float(input('Digite o valor do cateto adjacente em cm: '))
co = float(input('Digite o valor do cateto oposto em cm: '))
hp = math.sqrt(math.pow(ca,2) + math.pow(co,2))
print('-'*35)
print('O valor da hipotenusa é de {} cm!'.format(math.trunc(hp)))
