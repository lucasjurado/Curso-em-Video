total = c = 0
while True:
    peso = float(input('Digite o peso do peixe (kg): '))
    total += peso
    c += 1
    again = str(input('Próximo peixe [S/N]: ')).upper().strip()[0]
    if again == 'N':
        break
if total <= 25:
    cst = total * 10
else:
    cst = total * 15
print(f'O peso total de {c} peixes foi de {total} kg. O valor total a ser pago é de R$ {cst}.')