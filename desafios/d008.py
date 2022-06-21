valor_metros = float(input('Digite um valor em metros: '))

cm = valor_metros*100
mm = cm * 10

print('O valor de {:.2f} em centímentros é igual a {:.2f}.'.format(valor_metros, cm))
print('O valor de {:.2f} em milímetro é igual a {:.2f}.'.format(valor_metros, mm))