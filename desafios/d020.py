from random import shuffle
nome1 = str(input('Primeiro aluno: ')).title()
nome2 = str(input('Segundo aluno: ')).title()
nome3 = str(input('Terceiro aluno: ')).title()
nome4 = str(input('Quarto aluno: ')).title()

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('-'*10+'Ordem de apresentação'+'-'*10)
print('\033[;34m'+lista[0]+'\033[m')
print('\033[;34m'+lista[1]+'\033[m')
print('\033[;34m'+lista[2]+'\033[m')
print('\033[;34m'+lista[3]+'\033[m')
