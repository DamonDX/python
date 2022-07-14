import pygame

velocidade = float(input('Digite a velocidade do carro em km/hora: '))

if velocidade > 80:
    pygame.init()
    pygame.mixer.music.load('metalgears.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    multa = (velocidade - 80) * 7
    print('Você foi multado! Sua multa é de R${:.2f}!'.format(multa))
print('-' * 20 + 'FIM' + '-' * 20)
