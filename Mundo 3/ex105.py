from random import randint
from time import sleep
from operator import itemgetter

jogos = {}
print('Valores sorteados:')
for c in range (0,4):
    jogos[f'jogador{c+1}'] = randint(1,6)

for k, v in jogos.items():
    sleep(0.5)
    print(f' O {k} tirou {v}')

print('Ranking dos jogadores:')

ranking = sorted(jogos.items(), key = itemgetter(1), reverse = True)

for pos, n in enumerate(ranking):
    sleep(0.5)
    print(f' {pos+1}º: {n[0]} com {n[1]}')
