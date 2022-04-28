from random import randint   # Randomiza (escolhe) um número inteiro
from time import sleep       # Biblioteca time, com funções de controle de tempo
print('=== JOGO DA ADIVINHAÇÃO === ')
computador = randint(0, 10)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número inteiro em pensei? 🤔 '))    # O jogador tenta adivnhar o número
print('Precessando...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'HAHA! Eu te venci! Pensei no número {computador} e não no número {jogador}.')
print('-=-=-=-=-=-= FIM -=-=-=-=-=-=')
