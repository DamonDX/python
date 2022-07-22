# Usando strings
numero = input('Digite um numero de 0 a 9999: ')

# Unidade
print('Unidade: {}{}{}'.format('\033[;32m', numero[3:4], '\033[m'))
# Dezenas
print('Dezena: {}{}{}'.format('\033[;33m', numero[2:3], '\033[m'))
# Centezas
print('Centena: {}{}{}'.format('\033[;34m', numero[1:2], '\033[m'))
# Milhar
print('Milhar: {}{}{}'.format('\033[;35m', numero[:1], '\033[m'))

# Usando numeros inteiros
numero_inteiro = int(input('Digite um numero de 0 a 9999: '))

# É preciso fazer uma conversão
numero_inteiro = str(numero_inteiro)
# Unidade
print('Unidade: {}{}{}'.format('\033[;32m', numero_inteiro[3:4], '\033[m'))
# Dezenas
print('Dezena: {}{}{}'.format('\033[;33m', numero_inteiro[2:3], '\033[m'))
# Centezas
print('Centena: {}{}{}'.format('\033[;34m', numero_inteiro[1:2], '\033[m'))
# Milhar
print('Milhar: {}{}{}'.format('\033[;35m', numero_inteiro[:1], '\033[m'))
