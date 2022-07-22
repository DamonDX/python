from math import trunc

numero = float(input('Digite um número flutuante: '))

# Printando um número sem virgula.
numero_transformado = str(numero.__trunc__())
print('numero sem virgula: \033[;35m'+numero_transformado+'\033[m')