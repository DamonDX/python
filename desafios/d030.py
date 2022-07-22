numero = int(input('Digite um numero: '))

par_impar = numero % 2
print('O numero é \033[;30;41mIMPAR!\033[m' if par_impar > 0 else 'O número é \033[;30;43mPAR!\033[m')
