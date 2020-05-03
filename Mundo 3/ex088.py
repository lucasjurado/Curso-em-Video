clas = ('Flamengo','Santos','Palmeiras','Gremio','Athletico-Pr',
        'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
        'Goias', 'Bahia', 'Vasco', 'Atlético-Mg', 'Fluminense',
        'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')

lib = clas[0:6]
reb = clas[-4:]
alf = sorted(clas)
sp = clas.index('São Paulo') + 1
n = 1

for t in clas:
    print(f'{n}º - {t}')
    n += 1
print('-=-'*100)
print(f'Classificados diretamente para a Libertadores 2020: {lib}.')
print('-=-'*100)
print(f'Rebaixados para a série B: {reb}.')
print('-=-'*100)
print(f'Clubes em ordem alfabética: {alf}.')
print('-=-'*100)
print(f'São Paulo terminou na {sp}º posição!')
print('-=-'*100)

tim = str(input('Qual clube você gostaria de saber a classificação?: '))
esc = clas.index(tim) + 1
print(f'O clube {tim} terminou o campeonato na {esc}º posição!')
print('-=-'*100)