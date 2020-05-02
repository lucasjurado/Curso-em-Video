def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um nº inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: O usuário não informou os dados.\033[m')
            return 0
        else:
            return n

def leiafloar(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um nº real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: O usuário não informou os dados.\033[m')
            return 0
        else:
            return n


nint = leiaint('Digite um número inteiro: ')
nfloat = leiafloar('Digite um número real: ')

print(f'Número inteiro: {nint}; E o número real: {nfloat}.')

