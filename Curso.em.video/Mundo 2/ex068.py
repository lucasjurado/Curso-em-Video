sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'\033[31m{sexo}\033[m não foi reconhecido.\n'
                     f'Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo \033[36m{sexo}\033[m registrado com sucesso!')