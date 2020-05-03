import random
p=str(input('Primeiro aluno: '))
s=input('Segundo aluno: ')
t=input('Terceiro aluno: ')
q=input('Quarto aluno: ')
lista = [p,s,t,q]
print('O aluno escolhido foi {}'.format(random.choice(lista)))