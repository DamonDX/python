numero = int(input('Digite um ano: '))

# Para que o número seja bissexto ele deve ser multiplo de 4 e não deve ser multiplo de 100.
if numero % 4 == 0 and numero % 100 != 0:
    print('O ano é \033[;30;42mbissexto!\033[m')
else:
    print('O ano \033[;30;41mnão é bissexto!\033[m')
