vlr_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = float(input('Em quantos anos você deseja financiar a casa? '))
parcela = vlr_casa/(anos*12)

print(f'Para pagar uma casa de R$ {vlr_casa:.2f} em {anos:.0f} anos, a prestação será de R$ {parcela:.2f}.')

if parcela <= 0.3*salario:
    print('Empréstimo CONCEDIDO!!!')
elif parcela > 0.3*salario:
    print('Empréstimo NEGADO!!!')

