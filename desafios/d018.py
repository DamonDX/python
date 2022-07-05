from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))


print('O angulo de {} tem o SENO de {:.2f}' .format(angulo, seno))
print('O angulo de {} tem seu COSSENO de {:.2f}' .format(angulo, cosseno))
print('O angulo de {} tem sua TANGENTE de {:.2f}' .format(angulo,tangente))