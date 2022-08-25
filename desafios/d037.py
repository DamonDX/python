numero = int(input('Digite um número inteiro: '))

print('Escolha qual conversão você deseja fazer.')
print('1 - Binario')
print('2 - octal')
print('3 - hexadecimal')

# Escolha que o usuário irá fazer
escolha = str(input())

# Número binario.
if escolha == '1':
    binario = bin(numero)
    # Tive que fazer um fatiamento devido ao python usar '0b' para indicar que o número é binario.
    print('O valor de {} em binario é igual a {}.'.format(numero, binario[2:len(binario)]))
# Número octal.
elif escolha == '2':
    octal = oct(numero)
    print('O valor de {} em octal é {}.'.format(numero, octal[2:len(octal)]))
# Número hexadecimal.
elif escolha == '3':
    hexadecimal = hex(numero)
    print('O valor de {} em hexadecimal é {}.'.format(numero, hexadecimal[2:len(hexadecimal)]))
# Condição caso o usuário use outro número.
else:
    print('Erro. Você digitou um número errado.')
