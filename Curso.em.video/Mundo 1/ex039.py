p = float(input('Primeiro valor: '))
s = float(input('Segundo valor: '))
t = float(input('Terceiro valor: '))
'''if p > s and p > t:
    maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
print(f'O maior valor digitado foi {maior:.2f}.')
if p < s and p < t:
    menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
print('O menor valor digitado foi {:.2f}.'.format(menor))'''

num = [p,s,t]
print(f'O maior valor digitado foi {max(num):.2f}')
print(f'O menor valor digitado foi {min(num):.2f}')