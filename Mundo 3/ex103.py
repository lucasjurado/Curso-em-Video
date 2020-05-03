nm = []
lista = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    nm.append((n1+n2)/2)
    lista.append((nome,n1,n2))
    again = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if again == 'N':
        break
print('-=-'*20)
print(f'{"Nº":<4}{"NOME":<20}{"MÉDIA":^8}')
print('-'*35)
for pos, v in enumerate(lista):
    print(f'{pos:<4}{v[0]:<20}{nm[pos]:^8}')
print('-' * 35)
while True:
    lupa = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if lupa == 999:
        print('Finalizando...')
        break
    elif lupa <= len(lista) - 1:
        print(f'Notas de {lista[lupa][0]} foram {lista[lupa][1]} e {lista[lupa][2]}.')
    else:
        print(f'Código {lupa} não reconhecido. Tente novamente!')
