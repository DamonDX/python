nome = str(input('Qual é o seu nome? '))
# if nome.upper() == 'DAMON':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal.')

# Outra maneira de usar o if se o código for simples.
print('Que nome lindo você tem!' if nome.upper() == 'DAMON' else 'Seu nome é tão normal')
print('Bom dia, {}'.format(nome.title()))
