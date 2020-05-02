import random
import time
print('Vou escolher um número entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
lista = [0,1,2,3,4,5]
n = random.choice(lista)
esc = int(input('Em que número eu pensei? '))
print('Processando...')
time.sleep(3)
if n == esc:
    print('Parabéns! Eu também pensei no número {}.'.format(esc))
else:
    print('Errado! Eu pensei no número {}.'.format(n))
print('-=-'*30)
print('Fim do Jogo!')
