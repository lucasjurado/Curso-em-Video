def maior(*num):
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('O maior valor informado foi 0.')
    print('-' * 30)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()