dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro percorreu? '))

valor_a_pagar = (dias*60) + (km*0.15)

print('O valor a ser pago é igual a \033[;32mR${}\033[m'.format(valor_a_pagar))