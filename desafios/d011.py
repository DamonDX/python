altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
tintaL = area/2

print('A area tem {:.2f}m²'.format(area))
print('A quantidade de tinta em litros é {:.2f}(l)'.format(tintaL))