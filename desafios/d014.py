valor_c = float(input('Digite um um número em ºC: '))

valor_f = (1.8*valor_c) + 32

print('O valor de {}ºC é igual a \033[;31m{:.2f}ºF\033[m'.format(valor_c, valor_f))