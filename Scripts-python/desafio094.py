print('\033[1;30m===\033[m \033[1;35mGAME: PEDRA, PAPEL OU TESOURA\033[m \033[1;30m===\033[m')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[4;32mSuas opções:\033[m
\033[1;34m[ 0 ]\033[m \033[1;30mPedra\033[m
\033[1;34m[ 1 ]\033[m \033[1;30mPapel\033[m
\033[1;34m[ 2 ]\033[m \033[1;30mTesoura\033[m''')
jogador = int(input('\033[4;32mQual é a sua jogada?\033[m '))
print('\033[1;33mJO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PÔ!!!\033[m')
sleep(0.75)
print('\033[1;30mComputador jogou\033[m \033[1;34m{}\033[m\033[1;30m.\033[m'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[computador]))
if computador == 0:    # Computador jogou Pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('O JOGADOR VENCEU.')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU.')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 1:     # Computador jogou Papel
    if jogador == 0:
        print('O COMPUTADOR VENCEU.')
    elif jogador == 1:
        print('EMPATE.')
    elif jogador == 2:
        print('O JOGADOR VENCEU.')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 2:      # Computador jogou Tesoura
    if jogador == 0:
        print('O JOGADOR VENCEU.')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU.')
    elif jogador == 2:
        print('EMPATE.')
    else:
        print('JOGADA INVÁLIDA.')
#else:
print('\033[1;30m-=-=-=-=-=-=-=-=-=\033[m\033[1;33mPor Maxsuel Santos - 2020\033[m\033[1;30m-=-=-=-=-=-=-=-=-=-\033[m')
