valor = int(input('Digite um valor: '))

antecessor = valor - 1

sucessor = valor + 1

print('Antecessor do número \033[;34m{}\033[m é \033[;31m{}\033[m '
      'e o sucessor do número \033[;34m{}\033[m é \033[;31m{}\033[m.'
      .format( valor, antecessor, valor, sucessor))
