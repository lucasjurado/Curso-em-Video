import random
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
lista = [p,s,t,q]
ordem = random.sample(lista,k=4)
print('A ordem de apresentação será: {}.'.format(ordem))