distancia = float(input('Quantos km de distancia é a sua viagem: '))


if distancia <= 200:
    preco = distancia * 0.50
    print('O valor de sua passagem é {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor de sua passagem é {:.2f}'.format(preco))