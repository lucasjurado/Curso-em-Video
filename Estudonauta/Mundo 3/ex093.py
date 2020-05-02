listanum = []
pos_maior = []
pos_menor = []

for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))

print('=-='*40)
print(f'Você digitou os valores: {listanum}.')
maior = max(listanum)
menor = min(listanum)

for pos, val in enumerate(listanum):
    if val == maior:
        pos_maior.append(pos)
    elif val == menor:
        pos_menor.append(pos)

print(f'O maior valor digitado foi o {maior}, nas posições: {pos_maior}.\n'
      f'O menor valor digitado foi o {menor}, nas posições: {pos_menor}.')