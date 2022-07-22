valor = int(input('Digite um valor: '))

dobro = valor*2
triplo = valor*3
raiz = valor**(1/2)

print('O dobro de \033[;36m{}\033[m é \033[;33m{}\033[m.'.format(valor, dobro))
print('O tripo de \033[;36m{}\033[m é \033[;35m{}\033[m'.format(valor, triplo))
print('A raiz quadrada de \033[;36m{}\033[m é \033[;31m{}\033[m'.format(valor, raiz))
