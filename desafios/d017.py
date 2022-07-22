# from math import pow, sqrt
from math import hypot

cateto_oposto = float(input('Digite o cateto oposto de um triangulo retângulo: '))
cateto_adjacente = float(input('Digite o cateto adjacente de um triangulo retângulo: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
# hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
#
print('A hipotensa do triangulo retangulo é igual a {}{:.2f}{}'.format('\033[;36m', hipotenusa, '\033[m'))

