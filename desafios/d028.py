from random import randint
import pygame
import emoji


print('-' * 20 + 'Jogo de adivinhação' + '-' * 20)
jogador = int(input('De 0 a 5, adivinhe o número que o computador "pensou": '))
computador = randint(0, 5)
# Condição para dizer quem ganhou o jogo
if jogador == computador:
    print(emoji.emojize('\033[;34mVocê acertou! :sunglasses:\033[m', use_aliases=True))
    pygame.init()
    pygame.mixer.music.load('metalgears.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print(emoji.emojize('\033[;31mVocê perdeu... :sob:\033[m', use_aliases=True))
print('\033[;33mGAME OVER!\033[m')
