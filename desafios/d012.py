# Desconto de 5% de um produto.
valor_produto = float(input('Digite um valor em R$: '))

# Regra de três para pegar a porcentagem do produto subtrair sobre o valor do produto.
desconto = (valor_produto*5)/100
valor_a_pagar = valor_produto - desconto

print('O valor do produto com um desconto de \033[;34m5%\033[m é igual a \033[;32m{:.2f}\033[m'
      .format(valor_a_pagar))
