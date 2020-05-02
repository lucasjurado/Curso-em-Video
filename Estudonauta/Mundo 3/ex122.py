def ficha (nome, gol = 0):
    if nome =='':
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    return f'O jogador {nome} fez {gol} gol(s) no jogo.'


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

print(ficha(n,g))