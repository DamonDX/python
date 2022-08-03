nome = str(input('Qual é o seu nome? ')).title().strip()

if nome == 'Damon':
    print('Que nome bonito!')
elif nome == 'Gustavo' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))
