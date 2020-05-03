#import math
#num=int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é {}.'.format(num, math.floor(raiz)))

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {}.'.format(num, floor(raiz)))