from time import sleep

c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;43m',  # 2 - verde
     '\033[0;30;44m',  # 3 - azul
     '\033[7;30m',     # 4 - branco
        );

def msg(txt, cor = 0):
    print(c[cor], end='')
    print('~'*(len(txt)+4))
    print('  ', end='')
    print(f'{txt:^}')
    print('~'*(len(txt)+4))
    print(c[0],end='')

def ajuda (txt):
    print(c[4], end='')
    help(txt)
    print(c[0], end='')


while True:
    sleep(0.5)
    msg('SISTEMA DE AJUDA PyHELP', 2)
    sleep(0.5)
    f = str(input('Função ou Biblioteca > ')).strip()
    if f.upper() == 'FIM':
        sleep(0.5)
        msg('Fim do Programa!', 1)
        break
    sleep(0.5)
    msg(f"Acessando o manual do comando '{f}'", 3)
    sleep(0.5)
    ajuda(f)