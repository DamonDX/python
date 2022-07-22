from random import choice

nome = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo nome: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))

lista = [nome, nome2, nome3, nome4]
escolhido = choice(lista).strip()

print('O aluno que vai apagar o quadro é {}{}{}'.format('\033[;34m', escolhido.title(), '\033[m'))
