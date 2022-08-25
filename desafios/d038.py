numero = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))

if numero2 > numero:
    print('O número {} é maior que o numero {}'.format(numero2, numero))
elif numero > numero2:
    print('número {} é maior que o número {}'.format(numero, numero2))
else:
    print('Os números são IGUAIS!')
