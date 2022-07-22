lado_1 = float(input('Digite o comprimento de uma reta: '))
lado_2 = float(input('Digite outro comprimento de uma reta: '))
lado_3 = float(input('Digite outro comprimento de uma reta: '))

# A regra para poder se formar um triângulo é se as retas forem menores do que a soma de outras duas retas
if lado_1 < lado_2 + lado_3 and lado_2 < lado_3 + lado_1 and lado_3 < lado_2 + lado_1:
    print('\033[1;30;42mPodem\033[m formar um \033[4;30;43mtriângulo!\033[m')
else:
    print('\033[1;30;41mNão\033[m podem formar um \033[4;30;43mtriângulo!\033[m')