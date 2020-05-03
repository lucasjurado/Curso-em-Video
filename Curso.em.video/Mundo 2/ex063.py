frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range (len(junto)-1, -1, -1):
    inverso = inverso + junto[c]

print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print(f'{frase} é um PALINDROMO!')
else:
    print(f'{frase} NÃO é um PALINDROMO!')

