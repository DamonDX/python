import pygame

velocidade = float(input('Digite a velocidade do carro em km/hora: '))

if velocidade > 80:
    pygame.init()
    pygame.mixer.music.load('metalgears.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    multa = (velocidade - 80) * 7
    print('Você foi \033[4;30;41mmultado!\033[m Sua multa é de \033[;32mR${:.2f}\033[m!'.format(multa))
print('\033[;33m-\033[m' * 20 + '\033[;30;43mFIM' + '\033[;33m-\033[m' * 20)
