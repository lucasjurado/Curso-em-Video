num = c = sum = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    sum += num
    c += 1
print(f'A soma dos {c} valores foi de {sum}.')
