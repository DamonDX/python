numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))
numero_3 = float(input('Digite outro número: '))

# Verificando quem é o menor
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3

# Verifica quem é o maior
maior = numero_3
if numero_2 > numero_3 and numero_2 > numero_1:
    maior = numero_2
if numero_1 > numero_3 and numero_1 > numero_2:
    maior = numero_1

# Print do número maior e menor.
print('O maior número é o {}{}{}'.format('\033[;31m', maior, '\033[m'))
print('O menor número é o {}{}{}'.format('\033[;34m', menor, '\033[m'))
