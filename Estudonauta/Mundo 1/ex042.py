#teste com cores no terminal

nome=str(input('Digite seu\033[35m nome: \033[m'))
cores={'limpa': '\033[m',
       'azul' : '\033[34m',
       'amarelo' : '\033[33m'}

print('Olá {}{}{}, prazer em te conhecer!'.format(cores['azul'], nome, cores['limpa']))
