nome = input('Digite um nome: ').strip()

#Letras maiúsculas
print(nome.upper())
#Letras minúsculas
print(nome.lower())
#Numero de letras sem espaços
# print(len(nome.replace(" ", ""))) ---- outra maneira de fazer
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#Primeiro nome
#Primeiro fazer uma lista com a entranda do input
nome_lista = nome.split()
#Mostrar o número de caractes no primero nome
print(len(nome_lista[0]))