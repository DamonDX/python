#salvando nomes de uma pessoa famosa
nome = 'eric'
nome_famoso = 'albert'
sobrenome_famoso = 'einstein'

#nome completo do famoso
nome_completo_famoso = nome_famoso + " " + sobrenome_famoso

#sitação
sitacao = '"Uma pessoa que nunca cometeu um erro jamais tentou nada novo"'

#Junato a sitação com o nome do famoso e printando em seguida
message= nome_completo_famoso.title() + ' certa vez disse: ' +sitacao
print('Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo"')
print(message)

#apenas alguns testes de strings
print('Olá ' +nome+', você gostaria de aprender um pouco de Python hoje?')
print('Olá ' +nome.lower()+', você gostaria de aprender um pouco de Python hoje?')
print('Olá ' +nome.upper()+', você gostaria de aprender um pouco de Python hoje?')
print('Olá ' +nome.title()+', você gostaria de aprender um pouco de Python hoje?')
nome_2 = '\n\tdamon '
print(nome_2.lstrip())
print(nome_2.rstrip())
print(nome_2.strip())

#Programa para mostrar a sitação de um famoso e alguns testes