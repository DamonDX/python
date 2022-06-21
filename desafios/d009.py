valor = int(input('Digite um valor: '))
'''
print('{} x {:2} = {}'.format(valor, 1, valor*1))
print('{} x {:2} = {}'.format(valor, 2, valor*2))
print('{} x {:2} = {}'.format(valor, 3, valor*3))
print('{} x {:2} = {}'.format(valor, 4, valor*4))
print('{} x {:2} = {}'.format(valor, 5, valor*5))
print('{} x {:2} = {}'.format(valor, 6, valor*6))
print('{} x {:2} = {}'.format(valor, 7, valor*7))
print('{} x {:2} = {}'.format(valor, 8, valor*8))
print('{} x {:2} = {}'.format(valor, 9, valor*9))
'''
print('-'*12)

for contador in range(1, 11):
    print('{} x {:2} = {}'.format(valor, contador, valor*contador))

print('-'*12)