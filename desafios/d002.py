print('Digite a data do seu nascimento.')
dia = int(input('Dia: '))
mes = str(input('Mês: '))
ano = int(input('Ano: '))

print(
    'Você nasceu no dia \033[0;34m{}\033[m de \033[0;32m{}\033[m de \033[;31m{}\033[m. Correto?'.format(dia, mes, ano))
