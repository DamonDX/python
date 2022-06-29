nome = 'eric'

nome_famoso = 'albert'
sobrenome_famoso = 'einstein'
nome_completo_famoso = nome_famoso + " " + sobrenome_famoso
sitacao = '"Uma pessoa que nunca cometeu um erro jamais tentou nada novo"'

message= nome_completo_famoso.title() + ' certa vez disse: ' +sitacao
print('Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo"')
print(message)
print('Olá ' +nome+', você gostaria de aprender um pouco de Python hoje?')
print('Olá ' +nome.lower()+', você gostaria de aprender um pouco de Python hoje?')
print('Olá ' +nome.upper()+', você gostaria de aprender um pouco de Python hoje?')
print('Olá ' +nome.title()+', você gostaria de aprender um pouco de Python hoje?')
nome_2 = '\n\tdamon '
print(nome_2.lstrip())
print(nome_2.rstrip())
print(nome_2.strip())