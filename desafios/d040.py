import sys

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))

media = (nota_1 + nota_2)/2

# Tratamento de erros para números negativos.
if nota_1 < 0 or nota_2 < 0:
    print('Você digitou um valor invalido. Execute o programa novamente.')
    sys.exit()
if nota_1 > 10 or nota_2 > 10: # Tratamento de erros para números acima do aceitável.
    print('Você digitou um valor invalido. Execute o programa novamente.')
    sys.exit()

if 5.0 <= media < 7: # Condições da média do aluno
    print('Sou média é {}. Você ficou de RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua média é {}. Você foi APROVADO!'.format(media))
elif 5 > media > 0:
    print('Sua média é {}. Você foi REPROVADO!'.format(media))


