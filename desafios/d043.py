peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc = peso/(altura*altura)

print('O seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Seu peso está abaixo do normal!')
elif 18.5 <= imc <= 25:
    print('Você está com o peso ideal!')
elif 25 < imc <= 30:
    print('Você está com sobrepeso!')
elif 30 < imc <= 40:
    print('Você está com obsidade!')
else:
    print('Você está em obsidade mórbida!')
