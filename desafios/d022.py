nome = input('Digite um nome: ').strip()

# Letras maiúsculas
print('\033[;34m' + nome.upper() + '\033[m')
# Letras minúsculas
print('\033[;33m' + nome.lower() + '\033[m')
# Numero de letras sem espaços
# print(len(nome.replace(" ", ""))) ---- outra maneira de fazer
print('Seu nome tem ao todo {}{}{} letras'.format('\033[;35m', len(nome) - nome.count(' '), '\033[m'))
# Primeiro nome
# Primeiro fazer uma lista com a entranda do input
nome_lista = nome.split()
# Mostrar o número de caractes no primero nome
print('\033[;36m'+str(len(nome_lista[0]+'\033[m')))
