from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))


print('O angulo de {} tem o SENO de \033[;33m{:.2f}\033[m' .format(angulo, seno))
print('O angulo de {} tem seu COSSENO de \033[;35m{:.2f}\033[m' .format(angulo, cosseno))
print('O angulo de {} tem sua TANGENTE de \033[;36m{:.2f}\033[m' .format(angulo, tangente))