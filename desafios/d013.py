pagamento = float(input('Digite o valor do seu pagamento em R$:'))

aumento = (pagamento*15)/100
pagamento = pagamento + aumento

print('Voce teve um aumento e seu salário é de {}'.format(pagamento))
