real =  float(input('Quanto você tem na carteira? '))

dolar = real/5.14

print('Você tem {}US${:.2f}{}! Sinto muito...'.format('\033[;32m', dolar, '\033[m'))
