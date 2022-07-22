cidade = str(input('Em qual cidade você nasceu? ')).strip()

# Divisao das palavas para idenificar somente o primeiro nome.
dividido = cidade.split()
# Estou comparando tudo em mausculo para não ocorrer erro caso digite errado.
print('\033[;32m'+str('SANTO' in dividido[0].upper())+'\033[m')
