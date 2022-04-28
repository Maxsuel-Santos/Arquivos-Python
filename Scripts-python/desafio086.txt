print('\033[7;30m=== CONVERSOR DE BASES NUMÉRICAS ===\033[m')
from time import sleep
print('\033[1;33m-=-\033[m' * 25)
num = int(input('Digite um número inteiro: '))
print('\033[1;33m-=-\033[m' * 25)
print('''Escolha uma das bases para conversão: 
\033[1;32m[ 1 ]\033[m Converter para \033[1;30mBINÁRIO\033[m.
\033[1;32m[ 2 ]\033[m Converter para \033[1;34mOCTAL\033[m.
\033[1;32m[ 3 ]\033[m Converter para \033[1;35mHEXADECIMAL\033[m.''')
print('\033[1;33m-=-\033[m' * 25)
opcao = int(input('Sua opção: '))
print('\033[1;33m-=-\033[m' * 25)
print('\033[1;31mANALIZANDO...\033[m')
sleep(2)
print('\033[1;33m-=-\033[m' * 25)
if opcao == 1:
    print('\033[1;30m{}\033[m convertido para \033[1;30mBINÁRIO\033[m é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\033[1;30m{}\033[m convertido para \033[1;34mOCTAL\033[m é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\033[1;30m{}\033[m convertido para \033[1;33mHEXADECIMAL\033[m é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida. Tente os números \033[4;30m1\033[m\033[31m,'
          '\033[m \033[4;30m2\033[m \033[31me\033[m \033[4;30m3\033[m\033[31m.\033[m')
print('\033[1;33m-=-\033[m' * 25)
print('\033[7;30m-=-=-=-=-=FIM-=-=-=-=-=\033[m')
