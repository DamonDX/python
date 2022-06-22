pagamento = float(input('Digite o valor do seu pagamento em R$:'))

pagamento = pagamento + (pagamento*15)/100

print('Voce teve um aumento e seu salário se tornou  R${:.2f}'.format(pagamento))
