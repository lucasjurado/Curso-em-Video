lista =[]
for c in range (1,6):
    peso = float(input(f'Peso da {c}ª pessoa (kg): '))
    lista = lista + [peso]
print(f'O maior peso lido foi de {max(lista)} kg.\n'
      f'E o menor peso foi de {min(lista)} kg.')
