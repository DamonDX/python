from math import sqrt
from math import trunc

num = int(input('Digite um número: '))

raiz = sqrt(num)

print('A raiz de {} é {}!'.format(num, trunc(raiz)))
