altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
tintaL = area/2

print('A area tem {}{:.2f}m²{}'.format('\033[;31m', area, '\033[m'))
print('A quantidade de tinta em litros é {}{:.2f}(l){}'.format('\033[;36m', tintaL, '\033[m'))
