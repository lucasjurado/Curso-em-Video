import time
import random
cont = 1
print('Acabei de escolher um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
num = int(input('Qual o seu palpite? '))
print('Processando...')
time.sleep(0.5)
rand = random.randint(0,10)
while num != rand:
    if num > rand:
        num = int(input('Menos...Tente novamente: '))
        print('Processando...')
        time.sleep(0.5)
    else:
        num = int(input('Mais...Tente novamente: '))
        print('Processando...')
        time.sleep(0.5)
    cont +=1
print(f'Exato! Eu também pensei no número \033[36m{rand}\033[m. Você precisou de \033[36m{cont}\033[m chances para acertar!')