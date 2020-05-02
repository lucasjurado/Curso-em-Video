cad = {}
geral = []
apv = []

while True:
    cad.clear()
    apv.clear()
    cad['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas {cad["nome"]} jogou? '))
    for c in range (0,n):
        apv.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    cad['gols'] = apv[:]
    cad['total'] = sum(apv)
    geral.append(cad.copy())

    again = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if again in 'N':
        break
    print('-=-' * 20)
print('==='*20)

print('Cod ', end='')
for i in cad.keys():
    print(f'{i:<15}', end='')
print()
for pos, v in enumerate(geral):
    print(f'{pos:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('==='*20)

while True:
    busca = int(input('Buscar dados sobre o jogador: (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(geral):
        print(f'Código {busca} não reconhecido. Tente novamente!')
    else:
        print(f'Levantamento do jogador \033[36m{geral[busca]["nome"]}\033[m:')
        for pos, g in enumerate(geral[busca]["gols"]):
            print(f'Na {pos+1}ª partida fez {g} gols.')
    print('===' * 20)
print('Fim do Programa.')