pagamento = float(input('Digite o valor do seu pagamento em R$: '))

pagamento = pagamento + (pagamento*15)/100

print('Voce teve um aumento e seu salário se tornou \033[;32mR${:.2f}\033[m'.format(pagamento))
