nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1+nota2)/2

print('A média das das notas do aluno é \033[;31m{:.1f}\033[m!'.format(media))