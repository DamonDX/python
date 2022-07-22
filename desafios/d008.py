valor_metros = float(input('Digite um valor em metros: '))

cm = valor_metros*100
mm = cm * 10

print('O valor de \033[;34m{:.2f}\033[m em \033[4mcentímetros\033[m é igual a \033[;31m{:.2f}\033[m.'
      .format(valor_metros, cm))
print('O valor de \033[;34m{:.2f}\033[m em \033[4mmilímetro\033[m é igual a \033[;33m{:.2f}\033[m.'
      .format(valor_metros, mm))
