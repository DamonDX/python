import unidecode  #Modulo para tirar os acentos em uma string
frase = str(input('Diga uma frase: ')).strip()

#Variavel para guardar a string sem nenhuma acento para fazer comparação sem erros depois.
frase_sem_acento = unidecode.unidecode(frase)

#Printe de repetições da letra "A".
print('O número de vezes em que a letra "A" se repete é {}!'.format(frase_sem_acento.upper().count('A')))
#print da primeira aparição da letra "A".
print('Posição da letra "A" quando ela aparece pela primeira vez: {}'.format(frase_sem_acento.upper().find('A') + 1))
#print da ultima aparição da letra "A".
print('Ultima possição da letra "A": {}'.format(frase_sem_acento.upper().rfind('A') + 1))