def fatorial (n, show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O vlr do fatorial de um número n.
    """
    f = 1
    for c in range (n, 0, -1):
        f *= c
        if show == True and c > 1:
            print(c, end =' x ')
        elif show == True and c == 1:
            print(c, end =' = ')
    return f

print(fatorial(4, show = True))
print(fatorial(5))

help(fatorial)