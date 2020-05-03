cad = {}
apv = []

cad['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {cad["nome"]} jogou? '))
for c in range (0,n):
    apv.append(int(input(f'Quantos gols na partida {c+1}? ')))
cad['gols'] = apv[:]
cad['total'] = sum(apv)
print('-=-'*30)
for k, v in cad.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*30)
print(f'O jogador {cad["nome"]} jogou {n} partidas.')
for pos, g in enumerate(apv):
    print(f' => Na partida {pos+1}, fez {g} gols.')
print(f'Foi um total de {cad["total"]} gols.')