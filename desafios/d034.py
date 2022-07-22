salario = float(input('Digite o seu salário: '))

# Salário acima de R$: 1 250,00
if salario > 1250:
    aumento = (salario * 10) / 100
    salario = salario + aumento
    print('O seu salário aumentou de 10%, R$: {}{:.2f}{}'.format('\033[;32m', salario, '\033[m'))

# Salário abaixo de R$: 1 250.00
else:
    aumento = (salario * 15) / 100
    salario = salario + aumento
    print('O seu salário teve um aumento de 15%, R$: {}{:.2f}{}'.format('\033[;32m', salario, '\033[m'))
