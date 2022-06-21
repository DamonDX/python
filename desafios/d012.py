valor_produto = float(input('Digite um valor em R$:'))

desconto = (valor_produto*5)/100
valor_a_pagar = valor_produto - desconto

print('O valor do produto com um desconto de 5% é igual a {:.2f}'.format(valor_a_pagar))