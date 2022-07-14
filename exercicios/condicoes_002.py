nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2
print('A sua média foi {:.1f}'.format(media))
print('Sua média foi boa! Parabéns!!!' if media >= 6.0 else 'Sua média foi ruim... ESTUDE MAIS!')