n=input('Digite algo: ')
print('O tipo primitivo é da classe: ',type(n))
#print('o texto digitado é alpha?',n.isalpha())
print('o texto digitado é alpha? {}! é upper? {}! é alphanumeric? {}!'.format(n.isalpha(),n.isupper(),n.isalnum()))
print('Só tem espaços?',n.isspace())


