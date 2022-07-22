nome = str(input('Digite seu nome completo: '))

# Separando o nome commpleto em uma lista.
nome_completo = nome.split()

# Print do primeiro nome.
print('Primeiro nome: {}{}{}'.format('\033[;34m', nome_completo[0], '\033[m'))

# print do sobre nome.
# peguei o tamnho da lista de subtrair por um ja que ela começa em "0".
print('Sobre nome: {}{}{}'.format('\033[;36m', nome_completo[len(nome_completo) - 1], '\033[m'))
