lado_1 = float(input('Primeiro segmento: '))
lado_2 = float(input('Segundo segmento: '))
lado_3 = float(input('Terceiro segmento: '))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_3 + lado_1 and lado_3 < lado_2 + lado_1:
    print('Formar um \033[4;30;43mtriângulo!\033[m', end='')
    if lado_1 == lado_2 == lado_3:
        print(' É \033[1;30;44mEQUILÁTERO.\033[m')
    elif lado_1 != lado_2 != lado_3 != lado_1:
        print('É \033[1;30;41mESCALENO.\033[m')
    else:
        print(' \033[1;30;45mISÓSCELES.\033[m')
else:
    print('\033[1;30;41mNão\033[m podem formar um \033[4;30;43mtriângulo!\033[m')