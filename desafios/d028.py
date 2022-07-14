from random import randint
import pygame
import emoji


print('-' * 20 + 'Jogo de adivinhação' + '-' * 20)
jogador = int(5)#int(input('De 0 a 5, adivinhe o número que o computador "pensou": '))
computador = randint(0, 5)
# Condição para dizer quem ganhou o jogo
if jogador == computador:
    print(emoji.emojize('Você acertou! :sunglasses:', use_aliases=True))
    pygame.init()
    pygame.mixer.music.load('metalgears.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print(emoji.emojize('Você perdeu... :sob:', use_aliases=True))
print('GAME OVER!')
