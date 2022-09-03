print('{:=^40}'.format(' Loja '))
preco = float(input('Preço das compras: R$:'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x no cartão')
forma_pagamento = int(input('Qual é a opção? '))

if forma_pagamento == 1:
    desconto = (10*preco)/100
    preco_pagar = preco - desconto
    print('Você vai pagar {:.2f} com 10% de desconto'.format(preco_pagar))
elif forma_pagamento == 2:
    desconto = (5*preco)/100
    preco_pagar = preco - desconto
    print('Você vai pagar {:.2f} com 5% de desconto'.format(preco_pagar))
elif forma_pagamento == 3:
    parcelas = preco/2
    print('Você vai pagar 2x de {:.2f}'.format(parcelas))
elif forma_pagamento == 4:
    juros = (20*preco)/100
    parcelas = (preco + juros)/3
    print('Você vai pagar de 3x por {:.2f} com 20% de juros.'.format(parcelas))
else:
    print('Você digitou um valor não valido! Execute o programa novamente.')