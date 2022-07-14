# Usando strings
numero = input('Digite um numero de 0 a 9999: ')

# Unidade
print('Unidade: {}'.format(numero[3:4]))
# Dezenas
print('Dezena: {}'.format(numero[2:3]))
# Centezas
print('Centena: {}'.format(numero[1:2]))
# Milhar
print('Milhar: {}'.format(numero[:1]))

# Usando numeros inteiros
numero_inteiro = int(input('Digite um numero de 0 a 9999: '))

# É preciso fazer uma conversão
numero_inteiro = str(numero_inteiro)
# Unidade
print('Unidade: {}'.format(numero_inteiro[3:4]))
# Dezenas
print('Dezena: {}'.format(numero_inteiro[2:3]))
# Centezas
print('Centena: {}'.format(numero_inteiro[1:2]))
# Milhar
print('Milhar: {}'.format(numero_inteiro[:1]))
