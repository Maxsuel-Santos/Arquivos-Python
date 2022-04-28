print('\033[1;30m===\033[m \033[1;35mGERENCIADOR DE PAGAMENTOS\033[m \033[1;30m===\033[m')
print('     \033[1;30m===\033[m \033[1;35mLOJAS MAX ONE \033[m \033[1;30m===\033[m')
print('\033[1;33m-=-\033[m' * 25)
from time import sleep
produto = float(input('\033[1;30mQual o valor do produto?\033[m \033[1;31mR$\033[m '))
print('\033[1;33m-=-\033[m' * 25)
print('''\033[4;32mOPÇÕES DE PAGAMENTO:\033[m
 \033[1;34m[ 1 ]\033[m \033[1;30mÀ vista (Dinheiro/Cheque). 10% off.\033[m
 \033[1;34m[ 2 ]\033[m \033[1;30mÀ vista no cartão. 5% off.\033[m
 \033[1;34m[ 3 ]\033[m \033[1;30m2x no cartão. Sem descontos ou acréscimos.\033[m
 \033[1;34m[ 4 ]\033[m \033[1;30m3x ou mais no cartão. 20% de juros.\033[m''')
opcao = int(input('\033[4;32mSua escolha:\033[m '))
print('\033[1;33m-=-\033[m' * 25)
print('\033[1;31mANALIZANDO...\033[m')
sleep(2)
print('\033[1;33m-=-\033[m' * 25)
if opcao == 1:
    valor = produto - (produto * 10 / 100)
    print('\033[1;30mVocê vai pagar no total:\033[m \033[1;31mR$ {:.2f}\033[m'.format(valor))
elif opcao == 2:
    valor = produto - (produto * 5 / 100)
    print('\033[1;30mVocê vai pagar no total:\033[1;30m \033[1;31mR$ {:.2f}\033[m'.format(valor))
elif opcao == 3:
    valor = produto / 2
    print('\033[1;30mVocê irá pagar duas vezes de\033[m \033[1;31mR$ {:.2f}\033[1;31m '
          '\033[1;30mno total de\033[m \033[1;31mR$ {:.2f}\033[m'.format(valor, produto))
elif opcao == 4:
    valor = produto + (produto * 20 / 100)
    print('''\033[4;32mEscolha a opção de pagamento:\033[m
\033[1;34m[3x]
[4x]
[5x]\033[m''')
    opc = str(input('\033[4;32mSua escolha:\033[m ')).strip().lower()
    if opc == '3x':
        print('\033[1;30mVocê irá pagar\033[m \033[1;36m3x\033[m \033[1;30mde\033[m \033[1;31mR$ {:.2f}\033[m '
              '\033[1;30mno total de\033[m \033[1;31mR$ {:.2f}\033[m'.format((valor / 3), valor ))
    elif opc == '4x':
        print('\033[1;30mVocê irá pagar\033[m \033[1;36m4x\033[m \033[1;30mde\033[m \033[1;31mR$ {:.2f}\033[m '
              '\033[1;30mno total de\033[m \033[1;31mR$ {:.2f}\033[m'.format((valor / 4),valor))
    elif opc == '5x':
        print('\033[1;30mVocê irá pagar\033[m \033[1;36m5x\033[m \033[1;30mde\033[m \033[1;31mR$ {:.2f}\033[m '
              '\033[1;30mno total de\033[m \033[1;31mR$ {:.2f}\033[m'.format((valor / 5), valor))
    else:
        print('\033[1;31mOpção inválida. Tente entre\033[m \033[1;34m4x\033[m\033[1;31m,\033[m \033[1;34m5x\033[m '
              '\033[1;31me\033[m \033[1;34m6x\033[m\033[1;31m, por favor!\033[m')
else:
    print('\033[1;31mOpção inválida. Tente entre os números\033[m \033[1;34m1\033[m\033[1;31m,\033[m \033[1;34m2\033[m'
          '\033[1;31m,\033[m \033[1;34m3\033[m \033[1;31me\033[m \033[1;34m4\033[m\033[1;31m, por favor!\033[m')
print('\033[1;33m-=-\033[m' * 25)
print('\033[1;30m-=-=-=-=-=-=-=-=-=\033[m\033[1;33mPor Maxsuel Santos - 2020\033[m\033[1;30m-=-=-=-=-=-=-=-=-=-\033[m')
