print('\033[1;31m-=-\033[m' * 15)
print('=== JOGO DA ADIVINHAÇÃO V.2.0 ===')
print('\033[1;31m-=-\033[m' * 15)
from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você adivinha qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print(f'Acertou com {palpites} tentativas. Parabéns!')
