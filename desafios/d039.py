from datetime import date

sexo = str(input('Qual o seu sexo? (f/m)'))

if sexo == 'm':
    nascimento = int(input('Digite o ano em que você nasceu: '))
    ano = date.today().year

    idade = ano - nascimento

    print('Você nasceu em {} e tem {}'.format(nascimento, idade))

    if idade < 18:
        faltam = 18 - idade
        print('Você ainda não pode se alistar! Falta {} anos para se alistar.'.format(faltam))
        ano_alistamento = ano + faltam
        print('Voce vai se alistar no ano de {}.'.format(ano_alistamento))
    elif idade == 18:
        print('Você precisa se alistar agora!')
    else:
        passou = idade - 18
        print('Você perdeu o periodo de alistamento a {} anos'.format(passou))
        ano_alistamento = ano - passou
        print('Você deveria ter se alistado no ano de {}'.format(ano_alistamento))
elif sexo == 'f':
    print('Você não precisa fazer o alistamento obrigatório')
else:
    print('Você digitou um valor invalido!. digite novamente.')
    print('Obs: A letra "f" é para feminino e a letra "m" é para masculino.')