valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))


meses = anos*12
prestassao = valor/meses

if prestassao > (salario*30)/100:
    print('Você não pode fazer este empréstimo!')
else:
    print('você pode fazer o empréstimo.')
