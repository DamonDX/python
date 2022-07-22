import unidecode  # Modulo para tirar os acentos em uma string

frase = str(input('Diga uma frase: ')).strip()

# Variavel para guardar a string sem nenhuma acento para fazer comparação sem erros depois.
frase_sem_acento = unidecode.unidecode(frase)

# Printe de repetições da letra "A".
print('O número de vezes em que a letra \033[;32m"A"\033[m se repete é \033[;34m{}\033[m!'.format(frase_sem_acento.upper().count('A')))
# print da primeira aparição da letra "A".
print('Posição da letra \033[;32m"A"\033[m quando ela aparece pela primeira vez: \033[;34m{}\033[m'.format(frase_sem_acento.upper().find('A') + 1))
# print da última aparição da letra "A".
print('Ultima posição da letra \033[;32m"A"\033[m: \033[;34m{}\033[m'.format(frase_sem_acento.upper().rfind('A') + 1))
