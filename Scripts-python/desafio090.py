print('=== CLASSIFICANDO ATLETAS ===')
from datetime import date
atual = date.today().year
print('\033[1;33m-=-\033[m' * 25)
nasc = int(input('Seu ano de nascimento: '))
print('\033[1;33m-=-\033[m' * 25)
idade = atual - nasc
if idade <= 9:
    print(f'Você tem {idade} ano(s).')
    print('CATEGORIA: \033[1;34mMirim\033[m')
elif idade <= 14:
    print(f'Você tem {idade} ano(s).')
    print('CATEGORIA: \033[1;32mInfantil\033[m')
elif idade <= 19:
    print(f'Você tem {idade} ano(s).')
    print('CATEGORIA: \033[1;33mJúnior\033[m')
elif idade <= 25:
    print(f'Você tem {idade} ano(s).')
    print('CATEGORIA: \033[1;30mSênior\033[m')
else:
    print(f'Você tem {idade} ano(s).')
    print('CATEGORIA: \033[1;31mMaster\033[m')
print('\033[1;33m-=-\033[m' * 25)
print('\033[1;30m-=-=-=-=-=FIM-=-=-=-=-=\033[m')
