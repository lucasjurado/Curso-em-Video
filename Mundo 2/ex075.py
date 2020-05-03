c = s = num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        c += 1
        s += num
print(f'Você digitou {c} números e a soma entre eles foi de {s}.')