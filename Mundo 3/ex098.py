paren = []

exp = (str(input('Digite uma expressão matemática: '))).strip()
for c in exp:
    if '(' in c:
        paren.append(c)
    elif ')' in c:
        if '(' in paren:
            paren.pop()
        else:
            paren.append(c)
if len(paren) == 0:
    print(f'A expressão {exp} é valida.')
else:
    print(f'A expressão {exp} não é valida.')
print(paren)
