print('=== ÍNDICE DE MASSA CORPORAL ===')
print('\033[1;33m-=-\033[m' * 25)
massa = float(input('Informe sua massa corporal em Kg: '))
altura = float(input('Informe sua altura em metros: '))
print('\033[1;33m-=-\033[m' * 25)
imc = massa / (altura ** 2)
print('Seu IMC é de \033[4;30m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('Status: \033[1;31mABAIXO DO PESO\033[m.')
elif imc <= 25:
    print('Status: \033[1;32mPESO IDEAL\033[m.')
elif imc <= 30:
    print('Status: \033[1;30mSOBREPESO\033[m.')
elif imc <= 40:
    print('Status: \033[1;33mOBESIDADE\033[m.')
else:
    print('Status: \033[1;31mOBESIDADE MÓRBIDA\033[m.')
print('\033[1;33m-=-\033[m' * 25)
print('\033[1;30m-=-=-=-=-=-=-=-=-=\033[m\033[1;33mPor Maxsuel Santos - 2020\033[m\033[1;30m-=-=-=-=-=-=-=-=-=-\033[m')