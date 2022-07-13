nome = str(input('Digite seu nome completo: '))

#Separando o nome commpleto em uma lista.
nome_completo = nome.split()

#Print do primeiro nome.
print('Primeiro nome: {}'.format(nome_completo[0]))

#print do sobre nome.
#peguei o tamnho da lista de subtrair por um ja que ela começa em "0".
print('Sobre nome: {}'.format(nome_completo[len(nome_completo)-1]))
