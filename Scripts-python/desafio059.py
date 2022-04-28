print('\033[1;31m-=-\033[m' * 15)
print('\033[1;30m===\033[m \033[1;35mCRIANDO UM MENU DE OPÇÕES\033[m \033[1;30m===\033[1;30m')
print('\033[1;31m-=-\033[m' * 15)
from time import sleep
print('\033[1;33m=-=\033[m'*13)
n1 = float(input('\033[1;30mDigite um valor:\033[m '))
n2 = float(input('\033[1;30mDigite outro valor:\033[m '))
print('\033[1;33m=-=\033[m'*13)
print('\033[1;36mAnalisando...\033[1;30m')
sleep(1.5)
print('\033[1;33m=-=\033[m'*13)
opcao = 0
while opcao != 13:
    print('''\033[4;32mMenu de opções:\033[m 
        \033[1;34m[ 1 ]\033[m \033[1;30mSomar.\033[m
        \033[1;34m[ 2 ]\033[m \033[1;30mSubtrair.\033[m
        \033[1;34m[ 3 ]\033[m \033[1;30mMultiplicar.\033[m
        \033[1;34m[ 4 ]\033[m \033[1;30mDividir.\033[m
        \033[1;34m[ 5 ]\033[m \033[1;30mMaior.\033[m
        \033[1;34m[ 6 ]\033[m \033[1;30mMenor.\033[m
        \033[1;34m[ 7 ]\033[m \033[1;30mRaíz quadrada.\033[m
        \033[1;34m[ 8 ]\033[m \033[1;30mElevação ao quadrado.\033[m
        \033[1;34m[ 9 ]\033[m \033[1;30mCálculo de fatorial.\033[1;30m
        \033[1;34m[ 10 ]\033[m \033[1;30mPA (Progressão aritmética).\033[m
        \033[1;34m[ 11 ]\033[m \033[1;30mOuvir uma música.\033[m
        \033[1;34m[ 12 ]\033[m \033[1;30mNovos números.\033[m
        \033[1;34m[ 13 ]\033[m \033[1;30mSair do programa.\033[m''')
    opcao = int(input('\033[1;30m>>>\033[m \033[4;32mSua opção:\033[m '))
    print('\033[1;33m=-=\033[m' * 13)
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[1;30mA soma entre\033[m \033[1;31m{n1}\033[m \033[1;30me\033[m \033[1;31m{n2}\033[m '
              f'\033[1;30mfoi de\033[m \033[1;31m{soma}\033[1;33m')
    elif opcao == 2:
        sub = n1 - n2
        print(f'\033[1;30mA subtração entre\033[m \033[1;31m{n1}\033[m \033[1;30me\033[m \033[1;31m{n2}\033[m \033[1;30mfoi de\033[m \033[1;31m{sub}\033[m')
    elif opcao == 3:
        mult = n1 * n2
        print(f'\033[1;30mA multiplicação entre\033[m \033[1;31m{n1}\033[m \033[1;30me\033[m \033[1;31m{n2}\033[1;33m'
              f'\033[1;30m foi de\033[m \033[1;31m{mult}\033[1;33m')
    elif opcao == 4:
        div = n1 / n2
        print(f'\033[1;30mA divisão entre\033[m \033[1;31m{n1}\033[m \033[1;30me\033[m \033[1;31m{n2}\033[1;33m '
              f'\033[1;30mfoi de\033[m \033[1;31m{div:.2f}\033[m')
    elif opcao == 5:
        if n1 > n2:
            print(f'\033[1;30mO valor\033[m \033[1;31m{n1}\033[m \033[1;30mé maior.\033[m')
        else:
            print(f'\033[1;30mO valor\033[m \033[1;31m{n2}\033[m \033[1;30mé maior.\033[m')
    elif opcao == 6:
        if n1 < n2:
            print(f'\033[1;30mO valor\033[m \033[1;31m{n1}\033[m \033[1;30mé menor.\033[m')
        else:
            print(f'\033[1;30mO valor\033[m \033[1;31m{n2}\033[m \033[1;30mé menor.\033[1;30m')
    elif opcao == 7:
        raizqn1 = n1 ** (1/2)
        raizqn2 = n2 ** (1/2)
        print(f'\033[1;30mA raíz quadrada de\033[m \033[1;31m{n1}\033[m \033[1;30mé\033[m \033[1;31m{raizqn1:.2f}\033[m '
              f'\n\033[1;30mA raíz quadrada de\033[m \033[1;31m{n2}\033[m \033[1;30mé\033[1;30m \033[1;31m{raizqn2}\033[m')
    elif opcao == 8:
        print('\033[1;31m{}\033[m \033[1;30melevado ao quadrado é\033[1;30m \033[1;31m{}\033[m '
              '\n\033[1;31m{}\033[m \033[1;30melevado ao quadrado é\033[1;30m \033[1;31m{}\033[m'
              .format(n1, (n1 ** 2), n2, (n2 ** 2)))
    elif opcao == 9:
        from math import factorial
        num = int(input('\033[1;30mDigite um número para ver seu fatorial:\033[m '))
        print(f'\033[1;30mO fatorial de\033[m \033[1;31m{num}!\033[m \033[1;30mé\033[m '
              f'\033[1;31m{factorial(num)}\033[1;30m')
    elif opcao == 10:
        primeiro = int(input('\033[1;30mPrimeiro termo:\033[m '))
        razao = int(input('\033[1;30mRazão da PA:\033[m '))
        termo = primeiro
        contador = 1
        total = 0
        mais = 10
        while mais != 0:
            total += mais
            while contador <= total:
                print(f'\033[1;31m{termo}\033[m \033[1;31m-\033[m ', end='')
                contador += 1
                termo += razao
            print('\033[1;33mPAUSA\033[m')
            mais = int(input('\033[1;30m(Pressione 0 para terminar) Quantos termos você gostaria de ver '
                             'a mais?\033[1;30m '))
        print(f'\033[1;30mProgressão finalizada com\033[m \033[1;31m{total}\033[m \033[1;30mtermos mostrados.\033[m')
    elif opcao == 11:
        from pygame import mixer
        mixer.init()
        mixer.music.load('gta_v_theme.mp3')
        mixer.music.play()
        print('\033[1;33m---------------------------------------\033[m')
        input('\033[1;32mMúsica tema do GTA V. (2013, Rockstar.\033[1;30m)')
        print('\033[1;33m---------------------------------------\033[m')
    elif opcao == 12:
        print('\033[4;32mInforme os números novamente...\033[m')
        n1 = float(input('\033[1;30mDigite um valor:\033[m '))
        n2 = float(input('\033[1;30mDigite outro valor:\033[m '))
        print('\033[1;36mAnalisando...\033[m')
        sleep(1.5)
    elif opcao == 13:
        print('\033[1;34mFinalizando...\033[m')
    else:
        print('\033[1;31mOpção inválida. Tente novamente.\033[m')
    sleep(3)
    print('\033[1;33m=-=\033[m'*13)
print('\033[1;32mFim do programa. Volte sempre!\033[m')
print('\033[1;30mPor\033[m \033[1;34mMaxsuel Santos\033[m \033[1;30m- 2020\033[m')
