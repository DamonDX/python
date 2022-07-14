numero = int(input('Digite um ano: '))

# Para que o número seja bissexto ele deve ser multiplo de 4 e não deve ser multiplo de 100.
if numero % 4 == 0 and numero % 100 != 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
