lista_idade = []
h_idade = 0
nome_h_idade = ''
cont = 0

for c in range (1,5):
    print(f'-----{c} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    lista_idade = lista_idade + [idade]
    if c == 1 and sexo == 'M':
        h_idade = idade
        nome_h_idade = nome
    if sexo == 'M' and idade > h_idade:
        h_idade = idade
        nome_h_idade = nome
    if sexo == 'F' and idade < 20:
        cont += 1

media = sum(lista_idade)/4

print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {h_idade} anos e se chama {nome_h_idade}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos!')
