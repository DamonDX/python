from datetime import date
nascimento = int(input('Ano de nascimento: '))

ano = date.today().year
idade = ano - nascimento

if 0 <= idade < 9:
    print('O atleta tem {}'.format(idade))
    print('Classificação: MIRIM.')
elif 9 < idade <= 14:
    print('O atleta tem {}'.format(idade))
    print('Classificação: INFANTIL.')
elif 14 < idade <= 19:
    print('O atleta tem {}'.format(idade))
    print('Classificação: JÚNIOR.')
elif 19 < idade <= 25:
    print('O atleta tem {}'.format(idade))
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('O atleta tem {}'.format(idade))
    print('Classificação: MASTER')
elif idade < 0:
    print('Valor digitado inválido')
